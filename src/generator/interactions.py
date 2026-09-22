"""Typed interaction baseline for cooperation/competition experiments.

This module does not claim that biological sign patterns are optimal. It provides a
controlled way to compare positive/cooperative and negative/competitive edge classes
while holding topology fixed.
"""
from __future__ import annotations

from collections.abc import Iterable


def assign_interaction_signs(
    edges: Iterable[tuple[int, int]],
    *,
    competitive_fraction: float = 0.0,
    long_range: set[tuple[int, int]] | None = None,
    seed: int = 0,
) -> dict[tuple[int, int], int]:
    import random
    if not 0.0 <= competitive_fraction <= 1.0:
        raise ValueError("competitive_fraction must be in [0, 1]")
    rng = random.Random(seed)
    edge_list = list(set(edges))
    long_range = long_range or set()
    result = {}
    for edge in edge_list:
        p = competitive_fraction if edge in long_range else 0.0
        result[edge] = -1 if rng.random() < p else 1
    return result


def sign_fractions(signs: dict[tuple[int, int], int]) -> dict[str, float]:
    total = len(signs)
    if not total:
        return {"cooperative": 0.0, "competitive": 0.0}
    competitive = sum(v < 0 for v in signs.values())
    return {
        "cooperative": (total - competitive) / total,
        "competitive": competitive / total,
    }
