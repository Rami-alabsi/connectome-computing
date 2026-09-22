"""Higher-order module coordination primitives for M6 experiments.

Pairwise module messages are not assumed to be sufficient. A coordination simplex
allows a bounded joint state from several modules to be represented explicitly.
This is a classical experimental abstraction motivated by higher-order interaction
research; it is not a claim of quantum or biological equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

State = tuple[float, ...]
ModuleId = int
Simplex = tuple[ModuleId, ...]


@dataclass(frozen=True)
class CoordinationConfig:
    """Resource limits for higher-order coordination."""

    state_dim: int
    max_simplex_size: int = 3
    max_active_simplices: int | None = None

    def __post_init__(self) -> None:
        if self.state_dim < 1:
            raise ValueError("state_dim must be positive")
        if self.max_simplex_size < 2:
            raise ValueError("max_simplex_size must be at least 2")
        if self.max_active_simplices is not None and self.max_active_simplices < 1:
            raise ValueError("max_active_simplices must be positive")


def _mean_state(states: Sequence[Sequence[float]], dim: int) -> State:
    if not states:
        raise ValueError("at least one state is required")
    width = len(states[0])
    if width < dim:
        raise ValueError("state_dim exceeds source state dimension")
    if any(len(s) != width for s in states):
        raise ValueError("all states must have equal dimension")
    return tuple(sum(float(s[i]) for s in states) / len(states) for i in range(dim))


def build_coordination_simplices(
    module_states: Mapping[ModuleId, Sequence[float]],
    candidate_simplices: Sequence[Sequence[ModuleId]],
    *,
    config: CoordinationConfig,
) -> dict[Simplex, State]:
    """Construct bounded joint module states from candidate higher-order relations.

    Candidates are canonicalized, deduplicated, sorted, and truncated by a hard
    active-simplex budget. No node-level state is exposed directly.
    """
    canonical = set()
    for candidate in candidate_simplices:
        simplex = tuple(sorted(set(candidate)))
        if len(simplex) < 2 or len(simplex) > config.max_simplex_size:
            continue
        if any(module not in module_states for module in simplex):
            raise KeyError("every simplex module must have a state")
        canonical.add(simplex)

    selected = sorted(canonical)
    if config.max_active_simplices is not None:
        selected = selected[: config.max_active_simplices]

    return {
        simplex: _mean_state(
            [module_states[module] for module in simplex],
            config.state_dim,
        )
        for simplex in selected
    }
