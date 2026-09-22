"""Deterministic M6-COSMIC multiscale benchmark.

Generates a synthetic hierarchy and compares information-routing mechanisms under
explicit byte budgets. This is an engineering benchmark, not a biological or
physical simulation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from src.generator.capacity import build_capacity_hierarchy
from .relational_field import FieldConfig, build_global_field

Mode = Literal["full", "sparse", "field", "hybrid"]


@dataclass(frozen=True)
class MultiscaleCase:
    mode: Mode
    field_dim: int
    active_pairs: int
    bytes_per_value: int = 8


@dataclass(frozen=True)
class MultiscaleResult:
    mode: Mode
    nodes: int
    modules: int
    supermodules: int
    transmitted_values: int
    transmitted_bytes: int
    global_error: float
    pair_error: float


def _state(node: int, dim: int) -> tuple[float, ...]:
    # Deterministic bounded heterogeneous signal with both global and
    # pair-sensitive components. Bounded amplitude prevents absolute RMSE from
    # growing merely because the node index grows with benchmark scale.
    import math

    return tuple(
        math.sin((node + 1) * (i + 1) * 0.37)
        + 0.35 * math.cos((node % 17 + 1) * (i + 2) * 0.19)
        for i in range(dim)
    )


def _mean(states: list[tuple[float, ...]]) -> tuple[float, ...]:
    return tuple(sum(s[i] for s in states) / len(states) for i in range(len(states[0])))


def _rmse(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return (sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)) ** 0.5


def run_multiscale_case(
    *,
    nodes: int = 1000,
    module_capacity: int = 10,
    modules_per_parent: int = 10,
    state_dim: int = 8,
    case: MultiscaleCase,
) -> MultiscaleResult:
    """Run one deterministic multiscale information-routing condition."""
    if nodes < 2 or module_capacity < 1 or modules_per_parent < 1 or state_dim < 1:
        raise ValueError("invalid benchmark dimensions")
    if case.active_pairs < 1:
        raise ValueError("active_pairs must be positive")
    if case.field_dim < 1 or case.field_dim > state_dim:
        raise ValueError("field_dim must be within state dimension")

    hierarchy = build_capacity_hierarchy(
        nodes,
        module_capacity=module_capacity,
        modules_per_parent=modules_per_parent,
        hierarchy_depth=2,
    )
    node_states = {n: _state(n, state_dim) for n in range(nodes)}
    module_states = {
        m: _mean([node_states[n] for n in members])
        for m, members in enumerate(hierarchy.module_nodes)
    }
    target_global = _mean(list(module_states.values()))

    pair_modules = sorted(module_states)
    if len(pair_modules) < 2:
        raise ValueError("benchmark requires at least two modules")
    pair = (pair_modules[0], pair_modules[-1])
    target_pair = tuple(
        (module_states[pair[0]][i] + module_states[pair[1]][i]) / 2
        for i in range(state_dim)
    )

    if case.mode == "full":
        # Full reference exposes every module state.
        transmitted_values = len(module_states) * state_dim
        global_estimate = target_global
        pair_estimate = target_pair
    elif case.mode == "sparse":
        transmitted_values = min(case.active_pairs, len(module_states) - 1) * 2 * state_dim
        global_estimate = target_pair
        pair_estimate = target_pair
    else:
        field, report = build_global_field(
            module_states,
            config=FieldConfig(case.field_dim, case.bytes_per_value),
        )
        transmitted_values = report.transmitted_values
        # Decode a compact field to a state_dim vector by coordinate repetition.
        field_estimate = tuple(field[i % len(field)] for i in range(state_dim))
        global_estimate = field_estimate
        pair_estimate = field_estimate
        if case.mode == "hybrid":
            # Add a bounded explicit pair channel. This isolates the pair-sensitive
            # information without changing the global field payload.
            transmitted_values += 2 * state_dim * min(
                case.active_pairs, 1
            )
            pair_estimate = target_pair

    return MultiscaleResult(
        mode=case.mode,
        nodes=nodes,
        modules=len(hierarchy.module_nodes),
        supermodules=len(hierarchy.parent_modules),
        transmitted_values=transmitted_values,
        transmitted_bytes=transmitted_values * case.bytes_per_value,
        global_error=_rmse(global_estimate, target_global),
        pair_error=_rmse(pair_estimate, target_pair),
    )


def default_cases(
    *,
    state_dim: int = 8,
    field_dim: int = 2,
    active_pairs: int = 4,
) -> tuple[MultiscaleCase, ...]:
    """Return matched baseline conditions for the first scaling sweep."""
    return (
        MultiscaleCase("full", state_dim, active_pairs),
        MultiscaleCase("sparse", state_dim, active_pairs),
        MultiscaleCase("field", field_dim, active_pairs),
        MultiscaleCase("hybrid", field_dim, active_pairs),
    )
