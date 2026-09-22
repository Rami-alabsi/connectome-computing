"""Motif enrichment against degree-preserving null models.

For large connectomes, exhaustive 3-node enumeration is computationally infeasible.
This module therefore supports reproducible random triple sampling. Exact counting
remains available for small graphs.
"""
from __future__ import annotations

import math
import random
from collections import Counter
from itertools import combinations
from typing import Iterable

from .random_baseline import degree_preserving_randomization
from .triads import classify_triad


def triad_counts(edges: Iterable[tuple[str, str]]) -> Counter[str]:
    """Exhaustively count triads; intended for small graphs and validation."""
    edge_set = {(u, v) for u, v in edges if u != v}
    nodes = sorted({u for pair in edge_set for u in pair})
    counts: Counter[str] = Counter()
    for triple in combinations(nodes, 3):
        counts[classify_triad(triple, edge_set)] += 1
    return counts


def sampled_triad_counts(
    edges: Iterable[tuple[str, str]],
    *,
    samples: int = 10000,
    seed: int = 0,
) -> Counter[str]:
    """Estimate triad frequencies from uniformly sampled node triples."""
    edge_set = {(u, v) for u, v in edges if u != v}
    nodes = sorted({u for pair in edge_set for u in pair})
    if len(nodes) < 3:
        return Counter()

    rng = random.Random(seed)
    counts: Counter[str] = Counter()
    for _ in range(samples):
        triple = tuple(rng.sample(nodes, 3))
        counts[classify_triad(triple, edge_set)] += 1
    return counts


def motif_enrichment(
    edges: Iterable[tuple[str, str]],
    *,
    random_networks: int = 20,
    samples: int = 10000,
    swaps: int | None = None,
    seed: int = 0,
) -> dict[str, dict[str, float]]:
    """Compare sampled motif frequencies against degree-preserving null models."""
    edge_set = {(u, v) for u, v in edges if u != v}
    observed = sampled_triad_counts(edge_set, samples=samples, seed=seed)
    null_counts: dict[str, list[int]] = {name: [] for name in observed}

    for i in range(random_networks):
        randomized = degree_preserving_randomization(
            edge_set, swaps=swaps, seed=seed + i + 1
        )
        counts = sampled_triad_counts(
            randomized, samples=samples, seed=seed + i + 1
        )
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
