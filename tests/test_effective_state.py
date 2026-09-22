from src.simulator.effective_state import (
    InterfaceConfig,
    build_effective_messages,
    compress_mean,
)


def test_mean_compression_is_deterministic_and_dimension_limited():
    states = [(1, 2, 3, 4), (3, 4, 5, 6)]
    assert compress_mean(states, 2) == (2.0, 5.0)


def test_interface_collapses_node_edges_into_one_module_message():
    states = {
        0: (1.0, 2.0),
        1: (3.0, 4.0),
        2: (9.0, 10.0),
        3: (7.0, 8.0),
    }
    modules = {0: 0, 1: 0, 2: 1, 3: 1}
    edges = [(0, 2), (1, 2), (1, 3), (0, 3)]
    messages, report = build_effective_messages(
        states, edges, modules, config=InterfaceConfig(interface_dim=1)
    )
    assert messages == {(0, 1): (2.0,)}
    assert report.candidate_cross_edges == 4
    assert report.active_module_pairs == 1
    assert report.transmitted_values == 1
    assert report.transmitted_bytes == 8


def test_interface_pair_budget_drops_excess_pairs_deterministically():
    states = {i: (float(i), float(i + 1)) for i in range(6)}
    modules = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
    edges = [(0, 2), (0, 4), (2, 4), (4, 0), (2, 0)]
    messages, report = build_effective_messages(
        states, edges, modules, config=InterfaceConfig(interface_dim=1, max_module_pairs=2)
    )
    assert list(messages) == [(0, 1), (0, 2)]
    assert report.active_module_pairs == 2
    assert report.dropped_module_pairs == 1


def test_interface_preserves_local_state_by_only_emitting_cross_module_messages():
    states = {0: (1.0,), 1: (2.0,), 2: (3.0,)}
    modules = {0: 0, 1: 0, 2: 1}
    messages, report = build_effective_messages(
        states, [(0, 1), (1, 2)], modules, config=InterfaceConfig(interface_dim=1)
    )
    assert messages == {(0, 1): (2.0,)}
    assert report.candidate_cross_edges == 1
