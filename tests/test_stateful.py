from src.simulator.stateful import SimulatorConfig, step


def test_step_preserves_node_set_and_bounds_routes():
    states = {
        0: (1.0, 0.0),
        1: (0.5, 0.5),
        2: (0.0, 1.0),
        3: (0.2, 0.8),
    }
    edges = (
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 0),
        (3, 0),
    )
    modules = {0: 0, 1: 0, 2: 1, 3: 1}
    candidates = ((0, 1), (1, 0))

    next_states, report = step(
        states,
        edges,
        modules,
        candidates,
        config=SimulatorConfig(interface_dim=1, max_active_pairs=1),
    )

    assert set(next_states) == set(states)
    assert all(len(value) == 2 for value in next_states.values())
    assert report.routing.active_pairs <= 1
    assert report.transmitted_values <= 1


def test_step_is_deterministic_for_same_inputs():
    states = {
        0: (1.0, 0.0),
        1: (0.0, 1.0),
        2: (0.25, 0.75),
    }
    edges = ((0, 2), (2, 0), (1, 2))
    modules = {0: 0, 1: 1, 2: 2}
    candidates = ((0, 1), (1, 2), (2, 0))

    config = SimulatorConfig(interface_dim=1, max_active_pairs=2)
    first = step(states, edges, modules, candidates, config=config)
    second = step(states, edges, modules, candidates, config=config)

    assert first == second


def test_local_dynamics_run_without_cross_module_edges():
    states = {0: (1.0,), 1: (-1.0,)}
    modules = {0: 0, 1: 1}
    candidates = ((0, 1),)
    config = SimulatorConfig(interface_dim=1, max_active_pairs=1, coupling=0.5)

    next_states, report = step(
        states,
        (),
        modules,
        candidates,
        config=config,
    )

    assert report.active_module_pairs == 0
    assert report.transmitted_values == 0
    assert next_states[0][0] != states[0][0]
    assert next_states[1][0] != states[1][0]
