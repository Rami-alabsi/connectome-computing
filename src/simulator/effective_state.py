"""M6 effective-state interfaces for modular connectome-inspired computation.

Detailed node states remain local to their modules; only a bounded module-level
representation is exported across module boundaries. This is an experimental
classical abstraction, not a claim about quantum or biological computation.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Iterable, Mapping, Sequence

State = tuple[float, ...]
Edge = tuple[int, int]


@dataclass(frozen=True)
class InterfaceConfig:
    """Constraints applied to cross-module communication."""

    interface_dim: int
    max_module_pairs: int | None = None
    bytes_per_value: int = 8

    def __post_init__(self) -> None:
        if self.interface_dim < 1:
            raise ValueError("interface_dim must be positive")
        if self.max_module_pairs is not None and self.max_module_pairs < 1:
            raise ValueError("max_module_pairs must be positive when provided")
        if self.bytes_per_value < 1:
            raise ValueError("bytes_per_value must be positive")


@dataclass(frozen=True)
class CommunicationReport:
    """Resource accounting for one interface-construction step."""

    candidate_cross_edges: int
    active_module_pairs: int
    transmitted_values: int
    transmitted_bytes: int
    dropped_module_pairs: int


def _validate_state(state: Sequence[float]) -> State:
    if not state:
        raise ValueError("state vectors must be non-empty")
    return tuple(float(x) for x in state)


def compress_mean(states: Iterable[Sequence[float]], dimension: int) -> State:
    """Compress node states by deterministic mean pooling.

    If dimension is smaller than the node-state dimension, contiguous coordinate
    groups are averaged. This is a fixed baseline for the effective-state
    interface experiment; learned encoders belong in later experiments.
    """
    values = [_validate_state(s) for s in states]
    if not values:
        raise ValueError("at least one state is required")
    width = len(values[0])
    if any(len(v) != width for v in values):
        raise ValueError("all states must have the same dimension")
    if dimension < 1 or dimension > width:
        raise ValueError("interface dimension must be in [1, state dimension]")
    if dimension == width:
        return tuple(sum(v[i] for v in values) / len(values) for i in range(width))

    boundaries = [ceil(i * width / dimension) for i in range(dimension + 1)]
    return tuple(
        sum(v[i] for v in values for i in range(boundaries[j], boundaries[j + 1]))
        / (len(values) * (boundaries[j + 1] - boundaries[j]))
        for j in range(dimension)
    )


def build_effective_messages(
    node_states: Mapping[int, Sequence[float]],
    edges: Iterable[Edge],
    node_to_module: Mapping[int, int],
    *,
    config: InterfaceConfig,
) -> tuple[dict[tuple[int, int], State], CommunicationReport]:
    """Build one compact message per active directed module pair.

    Multiple node-level edges between the same modules are aggregated into one
    interface message. A hard module-pair budget can drop additional pairs
    deterministically by sorted pair identity.
    """
    pair_sources: dict[tuple[int, int], set[int]] = {}
    cross_edges = 0
    for u, v in edges:
        if u not in node_states or v not in node_states:
            raise KeyError("every edge endpoint must have a node state")
        if u not in node_to_module or v not in node_to_module:
            raise KeyError("every edge endpoint must have a module assignment")
        mu, mv = node_to_module[u], node_to_module[v]
        if mu == mv:
            continue
        cross_edges += 1
        pair_sources.setdefault((mu, mv), set()).add(u)

    pairs = sorted(pair_sources)
    dropped = 0
    if config.max_module_pairs is not None and len(pairs) > config.max_module_pairs:
        dropped = len(pairs) - config.max_module_pairs
        pairs = pairs[: config.max_module_pairs]

    messages: dict[tuple[int, int], State] = {}
    for pair in pairs:
        messages[pair] = compress_mean(
            (node_states[node] for node in sorted(pair_sources[pair])),
            config.interface_dim,
        )

    values = len(messages) * config.interface_dim
    report = CommunicationReport(
        candidate_cross_edges=cross_edges,
        active_module_pairs=len(messages),
        transmitted_values=values,
        transmitted_bytes=values * config.bytes_per_value,
        dropped_module_pairs=dropped,
    )
    return messages, report
