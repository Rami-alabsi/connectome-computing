from src.simulator.cosmic_benchmark import CosmicCase, run_cosmic_case


def test_field_and_hybrid_are_deterministic():
    states = {
        0: (1.0, 0.0, 0.0, 0.0),
        1: (3.0, 0.0, 0.0, 0.0),
        2: (5.0, 0.0, 0.0, 0.0),
        3: (7.0, 0.0, 0.0, 0.0),
    }
    pair = ((0, 1),)

    field = run_cosmic_case(
        states,
        CosmicCase("field", "field", 4, pair),
    )
    hybrid = run_cosmic_case(
        states,
        CosmicCase("hybrid", "hybrid", 4, pair),
    )

    assert field.transmitted_values == 4
    assert hybrid.transmitted_values == 12
    assert field.global_error == 0.0
    assert field.pair_error > 0.0
    assert hybrid.pair_error == 0.0


def test_sparse_pair_preserves_pair_information():
    states = {
        0: (1.0, 2.0),
        1: (3.0, 4.0),
        2: (10.0, 20.0),
    }
    result = run_cosmic_case(
        states,
        CosmicCase("sparse", "sparse", 1, ((0, 2),)),
    )

    assert result.transmitted_values == 4
    assert result.pair_error == 0.0
    assert result.global_error > 0.0
