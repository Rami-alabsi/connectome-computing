"""Dynamic relational layering primitives.

Engineering abstraction inspired by layered, multiplex, overlapping human
networks. This module is not a model of human social behavior.

A module may belong to multiple layers. Each candidate route has a layer label,
and a routing context can change the priority of layers while preserving an
explicit global communication budget.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

Pair = tuple[int, int]


@dataclass(frozen=True)
class RelationalLayer:
    name: str
    priority: float = 1.0
    max_active_pairs: int | None = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("layer name must be non-empty")
        if self.priority < 0:
            raise ValueError("layer priority must be non-negative")
        if self.max_active_pairs is not None and self.max_active_pairs < 1:
            raise ValueError("layer max_active_pairs must be positive")


@dataclass(frozen=True)
class LayeredRoute:
    source: int
    target: int
    layer: str
    score: float


@dataclass(frozen=True)
class LayeredRoutingConfig:
    max_active_routes: int
    bytes_per_route: int = 8

    def __post_init__(self) -> None:
        if self.max_active_routes < 1:
            raise ValueError("max_active_routes must be positive")
        if self.bytes_per_route < 1:
            raise ValueError("bytes_per_route must be positive")


@dataclass(frozen=True)
class LayeredRoutingReport:
    candidate_routes: int
    active_routes: int
    transmitted_bytes: int
    active_by_layer: tuple[tuple[str, int], ...]


def select_dynamic_layered_routes(
    candidates: Sequence[LayeredRoute],
    *,
    layers: Mapping[str, RelationalLayer],
    context_priority: Mapping[str, float] | None = None,
    config: LayeredRoutingConfig,
) -> tuple[tuple[LayeredRoute, ...], LayeredRoutingReport]:
    """Select routes using layer/context priority under a global route budget.

    The candidate graph and layer memberships remain fixed during a decision.
    Context changes route priority only. Duplicate (source, target, layer)
    candidates are collapsed deterministically.
    """
    context_priority = context_priority or {}
    unique: dict[tuple[int, int, str], LayeredRoute] = {}
    for route in candidates:
        if route.layer not in layers:
            raise KeyError(f"unknown layer: {route.layer}")
        key = (route.source, route.target, route.layer)
        if key not in unique or route.score > unique[key].score:
            unique[key] = route

    ranked = []
    for route in unique.values():
        layer = layers[route.layer]
        multiplier = context_priority.get(route.layer, layer.priority)
        effective_score = route.score * max(0.0, multiplier)
        ranked.append((effective_score, route))

    ranked.sort(
        key=lambda item: (-item[0], item[1].layer, item[1].source, item[1].target)
    )

    counts: dict[str, int] = {}
    selected: list[LayeredRoute] = []
    for effective_score, route in ranked:
        if len(selected) >= config.max_active_routes:
            break
        layer = layers[route.layer]
        used = counts.get(route.layer, 0)
        if layer.max_active_pairs is not None and used >= layer.max_active_pairs:
            continue
        selected.append(
            LayeredRoute(route.source, route.target, route.layer, effective_score)
        )
        counts[route.layer] = used + 1

    active_by_layer = tuple(sorted(counts.items()))
    report = LayeredRoutingReport(
        candidate_routes=len(unique),
        active_routes=len(selected),
        transmitted_bytes=len(selected) * config.bytes_per_route,
        active_by_layer=active_by_layer,
    )
    return tuple(selected), report
