"""Small, dependency-free directed canonical spatial maximum-entropy engine.

This module is deliberately limited to C3-A synthetic validation.  It is not
an FAFB-scale sampler and must not be used as one.
"""
from __future__ import annotations

import math
import random
from typing import Sequence


def sigmoid(x: float) -> float:
    if x >= 40.0:
        return 1.0
    if x <= -40.0:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))


def edge_probabilities(
    alpha: Sequence[float],
    beta: Sequence[float],
    lam: float,
    distances: Sequence[Sequence[float]],
) -> list[list[float]]:
    n = len(alpha)
    if len(beta) != n or len(distances) != n:
        raise ValueError("alpha, beta, and distances must have matching size")
    if lam < 0:
        raise ValueError("lam must be non-negative")
    for row in distances:
        if len(row) != n:
            raise ValueError("distances must be square")
    return [
        [
            0.0
            if i == j
            else sigmoid(alpha[i] + beta[j] - lam * distances[i][j])
            for j in range(n)
        ]
        for i in range(n)
    ]


def expected_statistics(
    probabilities: Sequence[Sequence[float]],
    distances: Sequence[Sequence[float]],
) -> tuple[list[float], list[float], float]:
    n = len(probabilities)
    out_degree = [sum(probabilities[i]) for i in range(n)]
    in_degree = [
        sum(probabilities[i][j] for i in range(n))
        for j in range(n)
    ]
    total_length = sum(
        probabilities[i][j] * distances[i][j]
        for i in range(n)
        for j in range(n)
    )
    return out_degree, in_degree, total_length


def _fit_degree_multipliers(
    target_out: Sequence[float],
    target_in: Sequence[float],
    distances: Sequence[Sequence[float]],
    lam: float,
    *,
    max_iter: int = 10_000,
    tolerance: float = 1e-10,
) -> tuple[list[float], list[float], float]:
    """Fit alpha/beta for a fixed lambda by iterative proportional scaling.

    The alpha/beta representation has a gauge freedom.  We fix it by enforcing
    mean(alpha) == 0 after each alternating row/column update.
    """
    n = len(target_out)
    if len(target_in) != n or len(distances) != n:
        raise ValueError("target vectors and distances must have matching size")
    if abs(sum(target_out) - sum(target_in)) > tolerance:
        raise ValueError("target in/out degree sums must agree")

    alpha = [0.0] * n
    beta = [0.0] * n

    for _ in range(max_iter):
        p = edge_probabilities(alpha, beta, lam, distances)
        current_out, current_in, _ = expected_statistics(p, distances)
        error = max(
            max(abs(current_out[i] - target_out[i]) for i in range(n)),
            max(abs(current_in[j] - target_in[j]) for j in range(n)),
        )
        if error <= tolerance:
            return alpha, beta, error

        for i in range(n):
            target = target_out[i]
            current = current_out[i]
            if target <= 0.0:
                alpha[i] = -40.0
            elif target >= n - 1:
                alpha[i] = 40.0
            elif current > 0.0:
                alpha[i] += math.log(target / current)

        p = edge_probabilities(alpha, beta, lam, distances)
        _, current_in, _ = expected_statistics(p, distances)
        for j in range(n):
            target = target_in[j]
            current = current_in[j]
            if target <= 0.0:
                beta[j] = -40.0
            elif target >= n - 1:
                beta[j] = 40.0
            elif current > 0.0:
                beta[j] += math.log(target / current)

        shift = sum(alpha) / n
        alpha = [x - shift for x in alpha]
        beta = [x + shift for x in beta]

    return alpha, beta, error


def fit_canonical_model(
    target_out: Sequence[float],
    target_in: Sequence[float],
    distances: Sequence[Sequence[float]],
    target_total_length: float,
    *,
    initial_lambda_high: float = 1.0,
    max_lambda_iter: int = 80,
    tolerance: float = 1e-9,
) -> tuple[list[float], list[float], float]:
    """Fit the C3-A directed canonical degree + wiring-length model.

    The target degree sequences are enforced in expectation.  Lambda is fitted
    by bisection against expected total wiring length.  This is a synthetic
    validation implementation only; it intentionally has no FAFB-scale
    sparse support approximation.
    """
    if target_total_length < 0:
        raise ValueError("target_total_length must be non-negative")

    def evaluate(lam: float):
        alpha, beta, degree_error = _fit_degree_multipliers(
            target_out, target_in, distances, lam, tolerance=tolerance
        )
        p = edge_probabilities(alpha, beta, lam, distances)
        _, _, total_length = expected_statistics(p, distances)
        return total_length - target_total_length, alpha, beta, degree_error

    low = 0.0
    flow, _, _, _ = evaluate(low)
    high = max(initial_lambda_high, 1e-12)
    fhigh, _, _, _ = evaluate(high)
    while flow * fhigh > 0.0 and high < 1e8:
        high *= 2.0
        fhigh, _, _, _ = evaluate(high)

    if flow * fhigh > 0.0:
        raise ValueError(
            "target wiring length is outside the bracketed canonical family"
        )

    for _ in range(max_lambda_iter):
        mid = (low + high) / 2.0
        fmid, alpha, beta, degree_error = evaluate(mid)
        if abs(fmid) <= tolerance and degree_error <= tolerance:
            return alpha, beta, mid
        if flow * fmid <= 0.0:
            high, fhigh = mid, fmid
        else:
            low, flow = mid, fmid

    fmid, alpha, beta, degree_error = evaluate((low + high) / 2.0)
    if abs(fmid) > 1e-6 or degree_error > 1e-6:
        raise RuntimeError(
            f"canonical fit did not converge: length_error={fmid}, "
            f"degree_error={degree_error}"
        )
    return alpha, beta, (low + high) / 2.0


def sample_graph(
    probabilities: Sequence[Sequence[float]],
    *,
    seed: int,
) -> set[tuple[int, int]]:
    """Sample one simple directed graph with independent Bernoulli edges."""
    rng = random.Random(seed)
    n = len(probabilities)
    edges: set[tuple[int, int]] = set()
    for i in range(n):
        if len(probabilities[i]) != n:
            raise ValueError("probabilities must be square")
        for j in range(n):
            if i != j and rng.random() < probabilities[i][j]:
                edges.add((i, j))
    return edges


def graph_statistics(
    edges: set[tuple[int, int]],
    distances: Sequence[Sequence[float]],
) -> tuple[list[int], list[int], float]:
    n = len(distances)
    out_degree = [0] * n
    in_degree = [0] * n
    total_length = 0.0
    for i, j in edges:
        if i == j:
            raise ValueError("self-loops are not allowed")
        out_degree[i] += 1
        in_degree[j] += 1
        total_length += distances[i][j]
    return out_degree, in_degree, total_length
