"""Motif enrichment against degree-preserving null models."""
from __future__ import annotations

import math
from collections import Counter
from itertools import combinations
from typing import Iterable

from .random_baseline import degree_preserving_randomization
from .triads import classify_triad


def triad_counts(edges: Iterable[tuple[str, str]]) -> Counter[str]:
    edge_set = {(u, v) for u, v in edges if u != v}
    nodes = sorted({u for pair in edge_set for u in pair})
    counts: Counter[str] = Counter()
    for triple in combinations(nodes, 3):
        counts[classify_triad(triple, edge_set)] += 1
    return counts


def motif_enrichment(
    edges: Iterable[tuple[str, str]],
    *,
    random_networks: int = 20,
    swaps: int | None = None,
    seed: int = 0,
) -> dict[str, dict[str, float]]:
    """Return observed count, null mean/std, z-score and enrichment."""
    edge_set = {(u, v) for u, v in edges if u != v}
    observed = triad_counts(edge_set)
    null_counts: dict[str, list[int]] = {name: [] for name in observed}

    for i in range(random_networks):
        randomized = degree_preserving_randomization(
            edge_set, swaps=swaps, seed=seed + i
        )
        counts = triad_counts(randomized)
        for name in null_counts:
            null_counts[name].append(counts.get(name, 0))

    result: dict[str, dict[str, float]] = {}
    for name, values in null_counts.items():
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std = math.sqrt(variance)
        observed_count = observed[name]
        result[name] = {
            "observed": float(observed_count),
            "null_mean": mean,
            "null_std": std,
            "z_score": (observed_count - mean) / std if std else 0.0,
            "enrichment": observed_count / mean if mean else float("inf"),
        }
    return result
