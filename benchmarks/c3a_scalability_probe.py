"""Methodological C3-A exact-support scaling probe.

This benchmark does not use FAFB data and does not implement a sparse support.
It evaluates every ordered non-self pair and accumulates expected wiring length
without materializing a probability matrix.

The coordinate distance is synthetic Euclidean distance only. It is a runtime
probe, not a biological result.
"""
from __future__ import annotations

import math
import random
import time


def sigmoid(x: float) -> float:
    if x >= 40.0:
        return 1.0
    if x <= -40.0:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))


def one_pass(n: int, seed: int = 123) -> float:
    rng = random.Random(seed)
    coords = [(rng.random(), rng.random()) for _ in range(n)]
    alpha = [rng.uniform(-1.0, 1.0) for _ in range(n)]
    beta = [rng.uniform(-1.0, 1.0) for _ in range(n)]

    start = time.perf_counter()
    total_length = 0.0
    for i, (xi, yi) in enumerate(coords):
        for j, (xj, yj) in enumerate(coords):
            if i == j:
                continue
            distance = math.hypot(xi - xj, yi - yj)
            probability = sigmoid(alpha[i] + beta[j] - distance)
            total_length += probability * distance
    elapsed = time.perf_counter() - start

    # Keep the calculation observable so an optimizing runtime cannot discard it.
    if not math.isfinite(total_length):
        raise RuntimeError("non-finite benchmark result")
    return elapsed


def main() -> None:
    for n in (32, 64, 128, 256, 512, 1024):
        elapsed = one_pass(n)
        pairs = n * (n - 1)
        print(f"N={n:4d} pairs={pairs:10d} seconds={elapsed:.6f}")


if __name__ == "__main__":
    main()
