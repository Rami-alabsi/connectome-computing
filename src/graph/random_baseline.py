"""Degree-preserving random baseline for directed connectome graphs.

Uses directed edge swaps. In-degree and out-degree sequences are preserved while
edge endpoints are rewired. Self-loops and duplicate directed pairs are avoided.
This is a null-model primitive, not a biological generative model.
"""
from __future__ import annotations

import random
from typing import Iterable


def degree_preserving_randomization(
    edges: Iterable[tuple[str, str]],
    *,
    swaps: int | None = None,
    seed: int = 0,
) -> set[tuple[str, str]]:
    current = {(u, v) for u, v in edges if u != v}
    if len(current) < 2:
        return current

    rng = random.Random(seed)
    edge_list = list(current)
    if swaps is None:
        swaps = max(10 * len(edge_list), 1000)

    successful = 0
    attempts = 0
    max_attempts = max(100, swaps * 20)

    while successful < swaps and attempts < max_attempts:
        attempts += 1
        i, j = rng.sample(range(len(edge_list)), 2)
        a, b = edge_list[i]
        c, d = edge_list[j]

        if a == d or c == b:
            continue

        new1, new2 = (a, d), (c, b)
        if new1 == new2 or new1 in current or new2 in current:
            continue

        current.remove((a, b))
        current.remove((c, d))
        current.add(new1)
        current.add(new2)
        edge_list[i], edge_list[j] = new1, new2
        successful += 1

    return current


def degree_sequence(edges):
    """Return directed in/out degree sequences for regression checks."""
    indeg = {}
    outdeg = {}
    for u, v in edges:
        outdeg[u] = outdeg.get(u, 0) + 1
        indeg[v] = indeg.get(v, 0) + 1
    return indeg, outdeg


def degree_preservation_report(original, randomized):
    """Report exact in/out-degree preservation and edge-count checks."""
    oi, oo = degree_sequence(original)
    ri, ro = degree_sequence(randomized)
    nodes = set(oi) | set(oo) | set(ri) | set(ro)
    return {
        "same_edge_count": len(set(original)) == len(set(randomized)),
        "same_in_degree": all(oi.get(n, 0) == ri.get(n, 0) for n in nodes),
        "same_out_degree": all(oo.get(n, 0) == ro.get(n, 0) for n in nodes),
    }
