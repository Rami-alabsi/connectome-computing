"""Three-node motif analysis for connectome graphs.

The implementation works on unique directed neuron pairs. Regional duplicate
rows should be aggregated before calling this module if regional identity is
not part of the motif definition.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from typing import Iterable


def directed_pairs(rows: Iterable[tuple[str, str]]) -> set[tuple[str, str]]:
    return {(a, b) for a, b in rows if a != b}


def triad_signature(nodes: tuple[str, str, str], edges: set[tuple[str, str]]) -> tuple[int, ...]:
    """Return the six directed edge bits for an ordered 3-node set."""
    a, b, c = nodes
    return tuple(int((u, v) in edges) for u, v in (
        (a, b), (b, a), (a, c), (c, a), (b, c), (c, b)
    ))


def count_triads(rows: Iterable[tuple[str, str]], limit_nodes: int | None = None) -> Counter[tuple[int, ...]]:
    """Count raw labeled 3-node signatures.

    This first implementation deliberately avoids imposing a graph-isomorphism
    taxonomy. The signatures are transparent and provide a reproducible baseline
    for the later canonical motif classifier.
    """
    edges = directed_pairs(rows)
    nodes = sorted({u for pair in edges for u in pair})
    if limit_nodes is not None:
        nodes = nodes[:limit_nodes]

    counts: Counter[tuple[int, ...]] = Counter()
    for triple in combinations(nodes, 3):
        counts[triad_signature(triple, edges)] += 1
    return counts
