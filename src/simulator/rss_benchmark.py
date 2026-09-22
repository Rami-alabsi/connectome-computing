"""Controlled Dynamic Relational State Space (RSS) benchmark.

The benchmark is an information-flow test: predictions may use only source
states represented by the active communication routes. This keeps topology,
routing, interface budget, and task information separate from the target.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import random
from typing import Sequence

State = tuple[float, ...]
Mode = str
Task = str

@dataclass(frozen=True)
class RSSCase:
    name: str
    mode: Mode
    field_dim: int = 2
    max_active_relations: int = 8
    max_higher_order: int = 2
    bytes_per_relation: int = 8
    seed: int = 0

@dataclass(frozen=True)
class RSSResult:
    case: str
    task: str
    context: int
    target: float
    prediction: float
    error: float
    active_relations: int
    transmitted_bytes: int
    routing_churn: int
    higher_order_relations: int

@dataclass(frozen=True)
class RSSSweepConfig:
    modules: int = 12
    state_dim: int = 4
    contexts: int = 3
    sequence_length: int = 9
    max_active_relations: int = 8
    max_higher_order: int = 2
    bytes_per_relation: int = 8

def _state(module: int, dim: int, seed: int) -> State:
    rng = random.Random(seed * 1009 + module * 9176)
    return tuple(
        math.sin((module + 1) * (i + 1) * 0.31)
        + 0.25 * math.cos((module % 7 + 1) * (i + 2) * 0.17)
        + 0.05 * rng.random()
        for i in range(dim)
    )

def _contexts(modules: int, contexts: int) -> tuple[tuple[int, ...], ...]:
    if contexts < 1:
        raise ValueError("contexts must be positive")
    groups = [[] for _ in range(contexts)]
    for module in range(modules):
        groups[module % contexts].append(module)
        if module % 4 == 0:
            groups[(module + 1) % contexts].append(module)
    return tuple(tuple(sorted(set(g))) for g in groups)

def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0

def _target(states: dict[int, State], task: Task, context: int,
            groups: tuple[tuple[int, ...], ...]) -> float:
    if task == "global":
        return _mean([s[0] for s in states.values()])
    if task == "pair":
        a, b = _pair_target(context, len(states))
        return 0.5 * (states[a][0] - states[b][0])
    group = groups[context % len(groups)]
    if task == "context":
        return _mean([states[m][1] for m in group])
    if task == "temporal":
        return _mean([states[m][2] for m in group])
    raise ValueError(f"unknown task: {task}")

def _pair_target(context: int, modules: int) -> tuple[int, int]:
    a = context % modules
    b = (a * 5 + 3) % modules
    return a, b

def _candidate_sources(case: RSSCase, states: dict[int, State],
                       groups: tuple[tuple[int, ...], ...], context: int,
                       task: Task) -> tuple[int, ...]:
    modules = len(states)
    group = groups[context % len(groups)]
    if task == "pair":
        a, b = _pair_target(context, modules)
        required = {a, b}
        if case.mode == "fixed_hierarchy":
            width = max(1, int(math.sqrt(modules)))
            parent = {m: m // width for m in states}
            required |= {m for m in states if parent[m] == parent[a]}
        elif case.mode in ("dynamic_layered", "dynamic_higher_order",
                           "fixed_overlap", "random_context"):
            required |= set(group)
        elif case.mode == "stable_core":
            required |= {0, 1, 2} | set(group)
        else:
            required |= set(range(modules))
        return tuple(sorted(required))
    if case.mode == "fixed_hierarchy":
        width = max(1, int(math.sqrt(modules)))
        parent = {m: m // width for m in states}
        return tuple(sorted(m for m in states if parent[m] == 0))
    if case.mode in ("dynamic_layered", "dynamic_higher_order",
                     "fixed_overlap"):
        if case.mode == "fixed_overlap":
            return tuple(sorted(set().union(*groups)))
        return tuple(sorted(group))
    if case.mode == "stable_core":
        return tuple(sorted(set(group) | {0, 1, 2}))
    return tuple(range(modules))

def _select_sources(case: RSSCase, states: dict[int, State],
                    groups: tuple[tuple[int, ...], ...], context: int,
                    task: Task) -> tuple[int, ...]:
    candidates = _candidate_sources(case, states, groups, context, task)
    budget = case.max_active_relations
    if not candidates or budget <= 0:
        return ()
    priority = set(groups[context % len(groups)])
    if case.mode == "dynamic_layered":
        ranked = sorted(candidates, key=lambda m: (-(m in priority), -abs(states[m][0]), m))
    elif case.mode == "dynamic_higher_order":
        ranked = sorted(candidates, key=lambda m: (-(m in priority), -abs(states[m][1]), m))
    elif case.mode == "flat_pairwise":
        ranked = sorted(candidates, key=lambda m: (-abs(states[m][0]), m))
    elif case.mode == "random_context":
        ranked = list(candidates)
        random.Random(case.seed * 100003 + context * 101 + len(task)).shuffle(ranked)
    elif case.mode == "stable_core":
        core = {0, 1, 2}
        ranked = sorted(candidates, key=lambda m: (-(m in core), -(m in priority), m))
    else:
        ranked = sorted(candidates)
    return tuple(ranked[:budget])

def _predict(case: RSSCase, states: dict[int, State], task: Task,
             context: int, groups: tuple[tuple[int, ...], ...],
             sources: tuple[int, ...]) -> float:
    if task == "pair":
        a, b = _pair_target(context, len(states))
        if a not in sources or b not in sources:
            return 0.0
        return 0.5 * (states[a][0] - states[b][0])
    group = set(groups[context % len(groups)])
    idx = 0 if task == "global" else (1 if task == "context" else 2)
    if case.mode == "dynamic_higher_order" and task in ("context", "temporal"):
        active_group = [m for m in sources if m in group]
        if len(active_group) >= 3 and case.max_higher_order > 0:
            return _mean([states[m][idx] for m in active_group])
    visible = [states[m][idx] for m in sources]
    return _mean(visible) if visible else 0.0

def run_rss_case(case: RSSCase, config: RSSSweepConfig) -> tuple[RSSResult, ...]:
    if config.modules < 3:
        raise ValueError("modules must be at least 3")
    states = {m: _state(m, config.state_dim, case.seed) for m in range(config.modules)}
    groups = _contexts(config.modules, config.contexts)
    previous: tuple[int, ...] = ()
    results = []
    for t in range(config.sequence_length):
        context = t % config.contexts
        for task in ("global", "pair", "context", "temporal"):
            sources = _select_sources(case, states, groups, context, task)
            target = _target(states, task, context, groups)
            prediction = _predict(case, states, task, context, groups, sources)
            churn = len(set(previous).symmetric_difference(sources))
            previous = sources
            ho = int(
                case.mode == "dynamic_higher_order"
                and task in ("context", "temporal")
                and len([m for m in sources if m in groups[context % len(groups)]]) >= 3
                and case.max_higher_order > 0
            )
            results.append(RSSResult(
                case.name, task, context, target, prediction,
                abs(target - prediction), len(sources),
                len(sources) * case.bytes_per_relation, churn, ho,
            ))
    return tuple(results)

def default_rss_cases(config: RSSSweepConfig) -> tuple[RSSCase, ...]:
    common = dict(max_active_relations=config.max_active_relations,
                  bytes_per_relation=config.bytes_per_relation)
    return (
        RSSCase("A_flat_pairwise", "flat_pairwise", **common),
        RSSCase("B_fixed_hierarchy", "fixed_hierarchy", **common),
        RSSCase("C_dynamic_layered", "dynamic_layered", **common),
        RSSCase("D_dynamic_higher_order", "dynamic_higher_order",
                max_higher_order=config.max_higher_order, **common),
        RSSCase("E_fixed_overlapping", "fixed_overlap", **common),
        RSSCase("F_random_context_matched", "random_context", **common),
        RSSCase("G_stable_core_flexible_periphery", "stable_core", **common),
    )
