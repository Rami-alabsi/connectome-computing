from src.simulator.coordination import (
    CoordinationConfig,
    build_coordination_simplices,
)


def test_coordination_simplices_are_canonical_and_deterministic():
    states = {0: (1.0, 2.0), 1: (3.0, 4.0), 2: (5.0, 6.0)}
    result = build_coordination_simplices(
        states,
        [(2, 1, 0), (0, 1, 2), (0, 1)],
        config=CoordinationConfig(state_dim=1, max_simplex_size=3),
    )
    assert result == {(0, 1): (2.0,), (0, 1, 2): (3.0,)}


def test_coordination_respects_simplex_size_and_budget():
    states = {i: (float(i),) for i in range(5)}
    result = build_coordination_simplices(
        states,
        [(0, 1), (0, 1, 2), (0, 1, 2, 3), (1, 3)],
        config=CoordinationConfig(state_dim=1, max_simplex_size=3, max_active_simplices=2),
    )
    assert list(result) == [(0, 1), (0, 1, 2)]


def test_coordination_does_not_expose_node_state():
    states = {0: (1.0, 2.0), 1: (3.0, 4.0)}
    result = build_coordination_simplices(
        states, [(0, 1)], config=CoordinationConfig(state_dim=2)
    )
    assert result[(0, 1)] == (2.0, 3.0)
