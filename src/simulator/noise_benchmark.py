"""Deterministic noise-robustness benchmark for M6-COSMIC.

This tests whether compact global and sparse explicit communication degrade
differently when module states are perturbed. It is an engineering control,
not a biological or physical simulation.
"""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal

from src.generator.capacity import build_capacity_hierarchy
from .multiscale_benchmark import _mean, _rmse, _state
from .relational_field import FieldConfig, build_global_field

NoiseMode = Literal["full", "sparse", "field", "hybrid"]


@dataclass(frozen=True)
class NoiseCase:
    mode: NoiseMode
    field_dim: int
    active_pairs: int
    noise_std: float
    seed: int = 0
    bytes_per_value: int = 8


@dataclass(frozen=True)
class NoiseResult:
    mode: NoiseMode
    nodes: int
    noise_std: float
    seed: int
    transmitted_values: int
    transmitted_bytes: int
    global_error: float
    pair_error: float


def _add_noise(
    state: tuple[float, ...], rng: random.Random, std: float
) -> tuple[float, ...]:
    return tuple(x + rng.gauss(0.0, std) for x in state)


def run_noise_case(
    *,
    nodes: int = 1000,
    module_capacity: int = 10,
    modules_per_parent: int = 10,
    state_dim: int = 8,
    case: NoiseCase,
) -> NoiseResult:
    if nodes < 2 or module_capacity < 1 or modules_per_parent < 1 or state_dim < 1:
        raise ValueError("invalid benchmark dimensions")
    if case.field_dim < 1 or case.field_dim > state_dim:
        raise ValueError("field_dim must be within state dimension")
    if case.active_pairs < 1 or case.noise_std < 0:
        raise ValueError("invalid noise configuration")

    hierarchy = build_capacity_hierarchy(
        nodes,
        module_capacity=module_capacity,
        modules_per_parent=modules_per_parent,
        hierarchy_depth=2,
    )
    node_states = {n: _state(n, state_dim) for n in range(nodes)}
    clean_modules = {
        m: _mean([node_states[n] for n in members])
        for m, members in enumerate(hierarchy.module_nodes)
    }
    target_global = _mean(list(clean_modules.values()))
    module_ids = sorted(clean_modules)
    pair = (module_ids[0], module_ids[-1])
    target_pair = tuple(
        (clean_modules[pair[0]][i] + clean_modules[pair[1]][i]) / 2
        for i in range(state_dim)
    )

    rng = random.Random(case.seed)
    noisy_modules = {
        m: _add_noise(clean_modules[m], rng, case.noise_std)
        for m in module_ids
    }

    if case.mode == "full":
        transmitted_values = len(noisy_modules) * state_dim
        global_estimate = _mean(list(noisy_modules.values()))
        pair_estimate = tuple(
            (noisy_modules[pair[0]][i] + noisy_modules[pair[1]][i]) / 2
            for i in range(state_dim)
        )
    elif case.mode == "sparse":
        active = min(case.active_pairs, len(module_ids) - 1)
        transmitted_values = active * 2 * state_dim
        selected = (module_ids[0], module_ids[min(active, len(module_ids) - 1)])
        global_estimate = tuple(
            (noisy_modules[selected[0]][i] + noisy_modules[selected[1]][i]) / 2
            for i in range(state_dim)
        )
        pair_estimate = tuple(
            (noisy_modules[pair[0]][i] + noisy_modules[pair[1]][i]) / 2
            for i in range(state_dim)
        )
    else:
        field, report = build_global_field(
            noisy_modules,
            config=FieldConfig(case.field_dim, case.bytes_per_value),
        )
        transmitted_values = report.transmitted_values
        global_estimate = tuple(field[i % len(field)] for i in range(state_dim))
        pair_estimate = global_estimate
        if case.mode == "hybrid":
            transmitted_values += 2 * state_dim * min(case.active_pairs, 1)
            pair_estimate = tuple(
                (noisy_modules[pair[0]][i] + noisy_modules[pair[1]][i]) / 2
                for i in range(state_dim)
            )

    return NoiseResult(
        mode=case.mode,
        nodes=nodes,
        noise_std=case.noise_std,
        seed=case.seed,
        transmitted_values=transmitted_values,
        transmitted_bytes=transmitted_values * case.bytes_per_value,
        global_error=_rmse(global_estimate, target_global),
        pair_error=_rmse(pair_estimate, target_pair),
    )
