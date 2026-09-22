from src.simulator.experiments import default_experiment_matrix, run_case


def test_experiment_matrix_contains_controlled_conditions():
    cases = default_experiment_matrix(full_state_dim=2, compressed_dim=1, active_pairs=2)
    assert [case.name for case in cases] == [
        "E0_full_fixed_all_candidates",
        "E1_full_sparse_fixed",
        "E2_compressed_fixed",
        "E3_compressed_state_dependent",
        "E4_compressed_state_dependent_pairwise",
    ]


def test_fixed_and_state_dependent_modes_are_explicit():
    states = {0: (1.0, 0.0), 1: (0.0, 1.0), 2: (0.9, 0.1)}
    edges = ((0, 1), (1, 2), (2, 0))
    modules = {0: 0, 1: 1, 2: 2}
    candidates = ((2, 0), (0, 1), (1, 2))

    cases = default_experiment_matrix(full_state_dim=2, compressed_dim=1, active_pairs=1)
    fixed = run_case(cases[1], states, edges, modules, candidates, full_state_dim=2)
    dynamic = run_case(cases[3], states, edges, modules, candidates, full_state_dim=2)

    assert fixed.report.routing.active_pairs == 1
    assert dynamic.report.routing.active_pairs == 1
    assert fixed.report.routing.transmitted_values == 2
    assert dynamic.report.routing.transmitted_values == 1
