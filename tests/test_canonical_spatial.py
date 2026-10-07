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
    return [[math.dist(a, b) for b in coords] for a in coords]


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
    assert abs(sum(fitted_alpha) / len(fitted_alpha)) < 1e-9
    assert abs(fitted_lam - lam) < 1e-6


def test_c3a_exact_enumeration_matches_analytic_moments():
    """For n=4, enumerate all 2^(n(n-1)) graphs and recover target moments."""
    distances = _distances([(0, 0), (1, 0), (0, 1), (1, 1)])
    probabilities = edge_probabilities(
        [0.2, -0.1, 0.0, 0.1],
        [0.1, -0.2, 0.05, 0.0],
        1.3,
        distances,
    )
    analytic_out, analytic_in, analytic_length = expected_statistics(
        probabilities, distances
    )
    pairs = [(i, j) for i in range(4) for j in range(4) if i != j]

    total_probability = 0.0
    enum_out = [0.0] * 4
    enum_in = [0.0] * 4
    enum_length = 0.0
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        probability = 1.0
        out = [0] * 4
        inn = [0] * 4
        length = 0.0
        for bit, (i, j) in zip(bits, pairs):
            p = probabilities[i][j]
            probability *= p if bit else (1.0 - p)
            if bit:
                out[i] += 1
                inn[j] += 1
                length += distances[i][j]
        total_probability += probability
        for i in range(4):
            enum_out[i] += probability * out[i]
            enum_in[i] += probability * inn[i]
        enum_length += probability * length

    assert abs(total_probability - 1.0) < 1e-12
    assert max(abs(a - b) for a, b in zip(analytic_out, enum_out)) < 1e-12
    assert max(abs(a - b) for a, b in zip(analytic_in, enum_in)) < 1e-12
    assert abs(analytic_length - enum_length) < 1e-12


def test_c3a_independent_sampling_recovers_ensemble_moments():
    distances = _distances([(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)])
    probabilities = edge_probabilities(
        [0.2, -0.1, 0.0, 0.1, -0.05],
        [0.1, -0.2, 0.05, 0.0, 0.15],
        1.3,
        distances,
    )
    target_out, target_in, target_length = expected_statistics(probabilities, distances)

    n_samples = 4000
    mean_out = [0.0] * 5
    mean_in = [0.0] * 5
    mean_length = 0.0
    for seed in range(n_samples):
        edges = sample_graph(probabilities, seed=seed)
        out, inn, length = graph_statistics(edges, distances)
        for i in range(5):
            mean_out[i] += out[i] / n_samples
            mean_in[i] += inn[i] / n_samples
        mean_length += length / n_samples

    assert max(abs(a - b) for a, b in zip(target_out, mean_out)) < 0.06
    assert max(abs(a - b) for a, b in zip(target_in, mean_in)) < 0.06
    assert abs(target_length - mean_length) < 0.10


def test_c3a_sampling_respects_support():
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


def test_c3a_graph_statistics_match_sample_structure():
    distances = _distances([(0, 0), (1, 0), (0, 1)])
    edges = {(0, 1), (2, 0)}
    out_degree, in_degree, total_length = graph_statistics(edges, distances)
    assert out_degree == [1, 0, 1]
    assert in_degree == [1, 1, 0]
    assert total_length == 2.0
