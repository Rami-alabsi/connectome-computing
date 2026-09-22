"""Deterministic state-dependent routing for M6 experiments.

This module makes routing an explicit resource-allocation step. Candidate module
pairs are fixed for a trial; the active subset is selected from current module
state, so topology and routing policy remain separable experimental factors.

This is a classical engineering baseline, not a biological mechanism.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Mapping, Sequence

State = tuple[float, ...]
ModuleId = int
Pair = tuple[ModuleId, ModuleId]


@dataclass(frozen=True)
class RoutingConfig:
    """Resource limits for one routing decision."""

    max_active_pairs: int
    bytes_per_value: int = 8
    values_per_message: int = 1

    def __post_init__(self) -> None:
        if self.max_active_pairs < 1:
            raise ValueError("max_active_pairs must be positive")
        if self.bytes_per_value < 1:
            raise ValueError("bytes_per_value must be positive")
        if self.values_per_message < 1:
            raise ValueError("values_per_message must be positive")


@dataclass(frozen=True)
class RoutingReport:
    candidate_pairs: int
    active_pairs: int
    dropped_pairs: int
    transmitted_values: int
    transmitted_bytes: int


def _norm(state: Sequence[float]) -> float:
    if not state:
        raise ValueError("module states must be non-empty")
    return sqrt(sum(float(x) * float(x) for x in state))


def select_state_dependent_routes(
    module_states: Mapping[ModuleId, Sequence[float]],
    candidate_pairs: Sequence[Pair],
    *,
    config: RoutingConfig,
) -> tuple[tuple[Pair, ...], RoutingReport]:
    """Select a bounded active route set using current module-state magnitude.

    The candidate topology is unchanged. Only which candidate pairs are active
    changes with state. Ties are resolved by pair identity for reproducibility.
    """

    scores: list[tuple[float, Pair]] = []
    seen: set[Pair] = set()
    for source, target in candidate_pairs:
        pair = (source, target)
        if pair in seen:
            continue
        seen.add(pair)
        if source not in module_states or target not in module_states:
            raise KeyError("every candidate endpoint must have a module state")
        score = _norm(module_states[source]) * _norm(module_states[target])
        scores.append((score, pair))

    scores.sort(key=lambda item: (-item[0], item[1]))
    selected = tuple(pair for _, pair in scores[: config.max_active_pairs])
    active = len(selected)
    candidate = len(scores)
    values = active * config.values_per_message
    report = RoutingReport(
        candidate_pairs=candidate,
        active_pairs=active,
        dropped_pairs=candidate - active,
        transmitted_values=values,
        transmitted_bytes=values * config.bytes_per_value,
    )
    return selected, report
