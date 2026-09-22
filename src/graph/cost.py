"""Resource-aware graph metrics for M5 validation."""
from __future__ import annotations
from math import dist
from typing import Hashable, Iterable, Mapping, Sequence

Edge = tuple[Hashable, Hashable]

def wiring_cost(edges: Iterable[Edge], positions: Mapping[Hashable, Sequence[float]]) -> float:
    """Return total Euclidean edge length for edges with known endpoints."""
    total = 0.0
    for source, target in edges:
        if source == target or source not in positions or target not in positions:
            continue
        total += dist(positions[source], positions[target])
    return total

def mean_edge_length(edges: Iterable[Edge], positions: Mapping[Hashable, Sequence[float]]) -> float:
    """Return mean Euclidean edge length over valid edges."""
    lengths = [dist(positions[source], positions[target]) for source, target in edges
               if source != target and source in positions and target in positions]
    return sum(lengths) / len(lengths) if lengths else 0.0

def communication_cost(edges: Iterable[Edge], positions: Mapping[Hashable, Sequence[float]] | None = None, *, distance_weight: float = 1.0, event_weight: float = 1.0) -> float:
    """Proxy cost = event count plus optional distance cost; not physical energy."""
    total = 0.0
    for source, target in edges:
        if source == target:
            continue
        total += event_weight
        if positions is not None and source in positions and target in positions:
            total += distance_weight * dist(positions[source], positions[target])
    return total

def cost_per_edge(edges: Iterable[Edge], positions: Mapping[Hashable, Sequence[float]] | None = None, *, distance_weight: float = 1.0, event_weight: float = 1.0) -> float:
    """Return communication cost normalized by valid directed edges."""
    edge_list = [(u, v) for u, v in edges if u != v]
    if not edge_list:
        return 0.0
    return communication_cost(edge_list, positions, distance_weight=distance_weight, event_weight=event_weight) / len(edge_list)
