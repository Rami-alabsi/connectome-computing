"""Controlled Dynamic Relational State Space (RSS) benchmark.

Classical engineering testbed comparing flat pairwise, fixed hierarchy,
dynamic overlapping layers, and bounded higher-order coordination under
matched active-relation and payload budgets.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import random
from typing import Sequence
from .coordination import CoordinationConfig, build_coordination_simplices
from .relational_layers import LayeredRoute, LayeredRoutingConfig, RelationalLayer, select_dynamic_layered_routes

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
        a = context % len(states)
        b = (a * 5 + 3) % len(states)
        return 0.5 * (states[a][0] - states[b][0])
    group = groups[context % len(groups)]
    if task == "context":
        return _mean([states[m][1] for m in group])
    if task == "temporal":
        return _mean([states[m][2] for m in group])
    raise ValueError(f"unknown task: {task}")

def _pair_candidates(modules: int) -> tuple[tuple[int, int], ...]:
    return tuple((a, b) for a in range(modules) for b in range(modules) if a != b)

def _layer_candidates(modules: int, groups: tuple[tuple[int, ...], ...]) -> tuple[LayeredRoute, ...]:
    routes = []
    for layer_id, group in enumerate(groups):
        layer = f"context-{layer_id}"
        for source in group:
            for target in group:
                if source != target:
                    score = 1.0 + ((source + 3 * target + layer_id) % 11) / 100.0
                    routes.append(LayeredRoute(source, target, layer, score))
    return tuple(routes)

def _route_selection(case: RSSCase, states: dict[int, State],
                     groups: tuple[tuple[int, ...], ...], context: int):
    budget = case.max_active_relations
    if case.mode == "flat_pairwise":
        candidates = _pair_candidates(len(states))
        ranked = sorted(candidates, key=lambda p: (-abs(states[p[0]][0] * states[p[1]][0]), p[0], p[1]))
        return tuple(ranked[:budget]), 0
    if case.mode == "fixed_hierarchy":
        width = max(1, int(math.sqrt(len(states))))
        parents = {m: m // width for m in states}
        ranked = sorted((a, b) for a in states for b in states if a != b and parents[a] == parents[b])
        return tuple(ranked[:budget]), 0
    layers = {f"context-{i}": RelationalLayer(f"context-{i}", priority=1.0, max_active_pairs=budget)
              for i in range(len(groups))}
    candidates = _layer_candidates(len(states), groups)
    priority = {f"context-{i}": (3.0 if i == context else 0.5) for i in range(len(groups))}
    selected, report = select_dynamic_layered_routes(
        candidates, layers=layers, context_priority=priority,
        config=LayeredRoutingConfig(max_active_routes=budget))
    return tuple((r.source, r.target) for r in selected), report.active_routes

def _predict(case: RSSCase, states: dict[int, State], task: Task, context: int,
             groups: tuple[tuple[int, ...], ...], routes: tuple[tuple[int, int], ...]) -> float:
    if case.mode == "fixed_hierarchy":
        width = max(1, int(math.sqrt(len(states))))
        parent = {m: m // width for m in states}
        selected_parent = context % (max(parent.values()) + 1)
        relevant = [m for m in states if parent[m] == selected_parent]
        if task == "global":
            return _mean([states[m][0] for m in states])
        if task == "pair":
            if not routes:
                return 0.0
            a, b = routes[0]
            return 0.5 * (states[a][0] - states[b][0])
        idx = 1 if task == "context" else 2
        return _mean([states[m][idx] for m in relevant]) if relevant else 0.0
    if task == "global":
        return _mean([s[0] for s in states.values()])
    if task == "pair":
        if not routes:
            return 0.0
        a, b = routes[0]
        return 0.5 * (states[a][0] - states[b][0])
    group = groups[context % len(groups)]
    idx = 1 if task == "context" else 2
    if case.mode == "dynamic_higher_order" and case.max_higher_order > 0 and len(group) >= 3:
        simplices = build_coordination_simplices(
            {m: states[m] for m in group}, [group[:3]],
            config=CoordinationConfig(state_dim=min(case.field_dim, len(states[group[0]])),
                                      max_simplex_size=3, max_active_simplices=case.max_higher_order))
        if simplices:
            return _mean([s[idx] for s in simplices[next(iter(simplices))]])
    sources = sorted(set(a for a, _ in routes) | set(b for _, b in routes))
    values = [states[m][idx] for m in sources if m in group]
    return _mean(values) if values else 0.0

def run_rss_case(case: RSSCase, config: RSSSweepConfig) -> tuple[RSSResult, ...]:
    if config.modules < 3:
        raise ValueError("modules must be at least 3")
    states = {m: _state(m, config.state_dim, case.seed) for m in range(config.modules)}
    groups = _contexts(config.modules, config.contexts)
    previous: tuple[tuple[int, int], ...] = ()
    results = []
    for t in range(config.sequence_length):
        context = t % config.contexts
        routes, _ = _route_selection(case, states, groups, context)
        churn = len(set(previous).symmetric_difference(routes))
        previous = routes
        for task in ("global", "pair", "context", "temporal"):
            target = _target(states, task, context, groups)
            prediction = _predict(case, states, task, context, groups, routes)
            ho = 1 if case.mode == "dynamic_higher_order" and task in ("context", "temporal") else 0
            results.append(RSSResult(case.name, task, context, target, prediction,
                                     abs(target - prediction), len(routes),
                                     len(routes) * case.bytes_per_relation, churn, ho))
    return tuple(results)

def default_rss_cases(config: RSSSweepConfig) -> tuple[RSSCase, ...]:
    return (
        RSSCase("A_flat_pairwise", "flat_pairwise", max_active_relations=config.max_active_relations,
                bytes_per_relation=config.bytes_per_relation),
        RSSCase("B_fixed_hierarchy", "fixed_hierarchy", max_active_relations=config.max_active_relations,
                bytes_per_relation=config.bytes_per_relation),
        RSSCase("C_dynamic_layered", "dynamic_layered", max_active_relations=config.max_active_relations,
                bytes_per_relation=config.bytes_per_relation),
        RSSCase("D_dynamic_higher_order", "dynamic_higher_order",
                max_active_relations=config.max_active_relations, max_higher_order=config.max_higher_order,
                bytes_per_relation=config.bytes_per_relation),
    )
