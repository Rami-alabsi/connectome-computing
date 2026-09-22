from src.simulator.routing import (
    RoutingConfig,
    select_state_dependent_routes,
)


def test_routing_is_state_dependent_and_budgeted():
    states = {
        0: (10.0, 0.0),
        1: (1.0, 0.0),
        2: (2.0, 0.0),
    }
    candidates = [(0, 1), (0, 2), (1, 2)]
    routes, report = select_state_dependent_routes(
        states,
        candidates,
        config=RoutingConfig(max_active_pairs=1),
    )
    assert routes == ((0, 2),)
    assert report.candidate_pairs == 3
    assert report.active_pairs == 1
    assert report.dropped_pairs == 2
    assert report.transmitted_bytes == 8


def test_routing_changes_when_current_state_changes():
    candidates = [(0, 1), (0, 2), (1, 2)]
    first, _ = select_state_dependent_routes(
        {0: (10.0,), 1: (1.0,), 2: (2.0,)},
        candidates,
        config=RoutingConfig(max_active_pairs=1),
    )
    second, _ = select_state_dependent_routes(
        {0: (1.0,), 1: (10.0,), 2: (2.0,)},
        candidates,
        config=RoutingConfig(max_active_pairs=1),
    )
    assert first != second


def test_routing_deduplicates_candidates_deterministically():
    states = {0: (1.0,), 1: (2.0,), 2: (3.0,)}
    routes, report = select_state_dependent_routes(
        states,
        [(0, 1), (0, 1), (1, 2)],
        config=RoutingConfig(max_active_pairs=2),
    )
    assert routes == ((1, 2), (0, 1))
    assert report.candidate_pairs == 2
