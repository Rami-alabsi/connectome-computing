"""Mesoscale organization metrics used by the M5 validation ladder.

These functions deliberately avoid assuming a biological taxonomy. Labels and
positions are supplied by the caller, so the same metrics can be applied to
real connectomes, synthetic graphs, and matched null models.

The module measures organization; it does not infer function.
"""

from __future__ import annotations

from collections import defaultdict
from math import dist
from typing import Hashable, Iterable, Mapping, Sequence, Tuple

Edge = Tuple[Hashable, Hashable]


def participation_coefficients(
    edges: Iterable[Edge],
    labels: Mapping[Hashable, Hashable],
) -> dict[Hashable, float]:
    """Return directed participation coefficients for nodes with outgoing edges.

    For node i, P_i = 1 - sum_c (k_i,c / k_i)^2, where k_i,c is the
    number of outgoing edges from i into module c. Self-loops are ignored.
    A node concentrated in one module has P≈0; a node distributing outputs
    across many modules has larger P. This is a descriptive mesoscale metric.
    """
    by_node: dict[Hashable, dict[Hashable, int]] = defaultdict(lambda: defaultdict(int))
    totals: dict[Hashable, int] = defaultdict(int)

    for source, target in edges:
        if source == target or source not in labels or target not in labels:
            continue
        module = labels[target]
        by_node[source][module] += 1
        totals[source] += 1

    result: dict[Hashable, float] = {}
    for node, total in totals.items():
        result[node] = 1.0 - sum((count / total) ** 2 for count in by_node[node].values())
    return result


def hierarchy_crossing_fraction(
    edges: Iterable[Edge],
    hierarchy: Mapping[Hashable, Sequence[Hashable]],
    level: int = 0,
) -> float:
    """Fraction of directed edges crossing labels at one hierarchy level."""
    total = 0
    crossing = 0
    for source, target in edges:
        if source not in hierarchy or target not in hierarchy:
            continue
        if level >= len(hierarchy[source]) or level >= len(hierarchy[target]):
            raise ValueError("hierarchy depth is smaller than requested level")
        if source == target:
            continue
        total += 1
        crossing += hierarchy[source][level] != hierarchy[target][level]
    return crossing / total if total else 0.0


def module_edge_fractions(
    edges: Iterable[Edge],
    labels: Mapping[Hashable, Hashable],
) -> dict[str, float]:
    """Return within-module and between-module edge fractions."""
    within = between = 0
    for source, target in edges:
        if source == target or source not in labels or target not in labels:
            continue
        if labels[source] == labels[target]:
            within += 1
        else:
            between += 1
    total = within + between
    if not total:
        return {"within_fraction": 0.0, "between_fraction": 0.0}
    return {"within_fraction": within / total, "between_fraction": between / total}


def long_range_fraction(
    edges: Iterable[Edge],
    positions: Mapping[Hashable, Sequence[float]],
    threshold: float,
) -> float:
    """Fraction of edges whose Euclidean length is >= threshold."""
    total = long_range = 0
    for source, target in edges:
        if source == target or source not in positions or target not in positions:
            continue
        total += 1
        if dist(positions[source], positions[target]) >= threshold:
            long_range += 1
    return long_range / total if total else 0.0


def hierarchy_distance(
    hierarchy: Mapping[Hashable, Sequence[Hashable]],
    source: Hashable,
    target: Hashable,
) -> int:
    """Return the first hierarchy level at which two nodes differ.

    Returns the common depth when all supplied levels match. This is useful
    for separating local, within-parent, and hierarchy-crossing connections.
    """
    if source not in hierarchy or target not in hierarchy:
        raise KeyError("source and target must exist in hierarchy")
    a, b = hierarchy[source], hierarchy[target]
    depth = min(len(a), len(b))
    for level in range(depth):
        if a[level] != b[level]:
            return level
    return depth
