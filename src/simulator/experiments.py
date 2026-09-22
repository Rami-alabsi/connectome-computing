"""Controlled experiment matrix for the M6 simulator.

The matrix keeps candidate topology fixed and varies only interface compression
and routing policy. It is a configuration layer; it does not execute training
or claim benchmark results.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

from .stateful import SimulatorConfig, StepReport, step

InterfaceMode = Literal["full", "compressed"]
RoutingMode = Literal["fixed", "state_dependent"]


@dataclass(frozen=True)
class ExperimentCase:
    """One matched-resource simulator condition."""

    name: str
    interface_mode: InterfaceMode
    routing_mode: RoutingMode
    interface_dim: int
    max_active_pairs: int

    def simulator_config(self, full_state_dim: int) -> SimulatorConfig:
        dimension = full_state_dim if self.interface_mode == "full" else self.interface_dim
        return SimulatorConfig(
            interface_dim=dimension,
            max_active_pairs=self.max_active_pairs,
        )


@dataclass(frozen=True)
class ExperimentResult:
    """One-step result plus explicit resource accounting."""

    case: str
    next_states: dict[int, tuple[float, ...]]
    report: StepReport


def default_experiment_matrix(
    *,
    full_state_dim: int,
    compressed_dim: int,
    active_pairs: int,
) -> tuple[ExperimentCase, ...]:
    """Return the initial E0-E4 controlled experiment matrix.

    E4 reserves a higher-order slot in the matrix documentation but remains
    pairwise here; higher-order coordination gets its own experiment family so
    that it cannot silently change multiple mechanisms at once.
    """
    if compressed_dim < 1 or compressed_dim > full_state_dim:
        raise ValueError("compressed_dim must be within full state dimension")
    if active_pairs < 1:
        raise ValueError("active_pairs must be positive")

    return (
        ExperimentCase("E0_full_fixed_all_candidates", "full", "fixed", full_state_dim, active_pairs),
        ExperimentCase("E1_full_sparse_fixed", "full", "fixed", full_state_dim, active_pairs),
        ExperimentCase("E2_compressed_fixed", "compressed", "fixed", compressed_dim, active_pairs),
        ExperimentCase("E3_compressed_state_dependent", "compressed", "state_dependent", compressed_dim, active_pairs),
        ExperimentCase("E4_compressed_state_dependent_pairwise", "compressed", "state_dependent", compressed_dim, active_pairs),
    )


def run_case(
    case: ExperimentCase,
    node_states: dict[int, Sequence[float]],
    node_edges: Sequence[tuple[int, int]],
    node_to_module: dict[int, int],
    candidate_pairs: Sequence[tuple[int, int]],
    *,
    full_state_dim: int,
) -> ExperimentResult:
    """Run one deterministic one-step case.

    Fixed routing uses a deterministic candidate-prefix policy; E0 is the
    all-candidate reference while E1-E4 use the supplied sparse active-pair budget.
    """
    if case.interface_mode == "full":
        dimension = full_state_dim
    else:
        dimension = case.interface_dim

    if case.name == "E0_full_fixed_all_candidates":
        config = SimulatorConfig(
            interface_dim=full_state_dim,
            max_active_pairs=max(1, len(set(candidate_pairs))),
            routing_mode="fixed",
        )
    else:
        base = case.simulator_config(full_state_dim)
        config = SimulatorConfig(
            interface_dim=base.interface_dim,
            max_active_pairs=base.max_active_pairs,
            routing_mode=case.routing_mode,
        )
    next_states, report = step(
        node_states,
        node_edges,
        node_to_module,
        candidate_pairs,
        config=config,
    )
    return ExperimentResult(case=case.name, next_states=next_states, report=report)
