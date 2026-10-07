import itertools
import math

from src.generator.canonical_spatial import (
    edge_probabilities,
    expected_statistics,
    fit_canonical_model,
    graph_statistics,
    sample_graph,
)


def _distances(coords):
    return [
        [math.dist(a, b) for b in coords]
        for a in coords
    ]


def test_c3a_recovers_known_directed_canonical_parameters():
    coords = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (2.0, 0.0)]
    distances = _distances(coords)

    alpha = [0.4, -0.2, 0.1, -0.3, 0.0]
    beta = [-0.1, 0.2, -0.4, 0.1, 0.2]
    lam = 2.0

    probabilities = edge_probabilities(alpha, beta, lam, distances)
    target_out, target_in, target_length = expected_statistics(probabilities, distances)

    fitted_alpha, fitted_beta, fitted_lam = fit_canonical_model(
        target_out, target_in, distances, target_length, initial_lambda_high=4.0
    )
    fitted = edge_probabilities(fitted_alpha, fitted_beta, fitted_lam, distances)
    out2, in2, length2 = expected_statistics(fitted, distances)

    assert max(abs(a - b) for a, b in zip(target_out, out2)) < 1e-7
    assert max(abs(a - b) for a, b in zip(target_in, in2)) < 1e-7
    assert abs(target_length - length2) < 1e-7

    # Gauge is fixed by mean(alpha)=0; parameters are therefore identifiable.
    assert abs(sum(fitted_alpha) / len(fitted_alpha)) < 1e-9
    assert abs(fitted_lam - lam) < 1e-6


def test_c3a_independent_sampling_respects_support():
    distances = _distances([(0, 0), (1, 0), (0, 1), (1, 1)])
    probabilities = edge_probabilities(
        [0.2, -0.1, 0.0, 0.1],
        [0.1, -0.2, 0.05, 0.0],
        1.3,
        distances,
    )
    for seed in range(5):
        edges = sample_graph(probabilities, seed=seed)
        assert all(i != j for i, j in edges)
        assert len(edges) <= 4 * 3


def test_c3a_exact_small_graph_partition_is_one():
    """For n=4, enumerate all 2^(n(n-1)) graphs and verify factorization."""
    distances = _distances([(0, 0), (1, 0), (0, 1), (1, 1)])
    probabilities = edge_probabilities(
        [0.2, -0.1, 0.0, 0.1],
        [0.1, -0.2, 0.05, 0.0],
        1.3,
        distances,
    )
    pairs = [(i, j) for i in range(4) for j in range(4) if i != j]

    total_probability = 0.0
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        probability = 1.0
        for bit, (i, j) in zip(bits, pairs):
            p = probabilities[i][j]
            probability *= p if bit else (1.0 - p)
        total_probability += probability

    assert abs(total_probability - 1.0) < 1e-12


def test_c3a_graph_statistics_match_sample_structure():
    distances = _distances([(0, 0), (1, 0), (0, 1)])
    edges = {(0, 1), (2, 0)}
    out_degree, in_degree, total_length = graph_statistics(edges, distances)

    assert out_degree == [1, 0, 1]
    assert in_degree == [1, 1, 0]
    assert total_length == 2.0
