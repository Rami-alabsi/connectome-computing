from src.simulator.multiscale_benchmark import (
    MultiscaleCase,
    default_cases,
    run_multiscale_case,
)


def test_multiscale_shape_and_budget_are_deterministic():
    case = MultiscaleCase("field", 2, 4)
    a = run_multiscale_case(nodes=100, module_capacity=10, case=case)
    b = run_multiscale_case(nodes=100, module_capacity=10, case=case)
    assert a == b
    assert a.nodes == 100
    assert a.modules == 10
    assert a.supermodules == 1
    assert a.transmitted_bytes == a.transmitted_values * 8


def test_hybrid_restores_pair_sensitive_information():
    field = run_multiscale_case(
        nodes=100, module_capacity=10,
        case=MultiscaleCase("field", 2, 4),
    )
    hybrid = run_multiscale_case(
        nodes=100, module_capacity=10,
        case=MultiscaleCase("hybrid", 2, 4),
    )
    assert hybrid.pair_error == 0.0
    assert field.pair_error >= hybrid.pair_error


def test_default_matrix_contains_all_control_families():
    names = {case.mode for case in default_cases()}
    assert names == {"full", "sparse", "field", "hybrid"}
