from src.simulator.noise_benchmark import NoiseCase, run_noise_case


def test_noise_benchmark_is_deterministic():
    case = NoiseCase("field", field_dim=2, active_pairs=4, noise_std=0.05, seed=7)
    a = run_noise_case(nodes=100, case=case)
    b = run_noise_case(nodes=100, case=case)
    assert a == b
    assert a.transmitted_bytes == a.transmitted_values * 8


def test_zero_noise_matches_clean_targets_for_full_condition():
    result = run_noise_case(
        nodes=100,
        case=NoiseCase("full", field_dim=8, active_pairs=4, noise_std=0.0),
    )
    assert result.global_error == 0.0
    assert result.pair_error == 0.0


def test_hybrid_preserves_noisy_pair_information():
    field = run_noise_case(
        nodes=100,
        case=NoiseCase("field", field_dim=2, active_pairs=4, noise_std=0.05, seed=3),
    )
    hybrid = run_noise_case(
        nodes=100,
        case=NoiseCase("hybrid", field_dim=2, active_pairs=4, noise_std=0.05, seed=3),
    )
    assert hybrid.pair_error <= field.pair_error
