from src.graph.cost import communication_cost, cost_per_edge, mean_edge_length, wiring_cost

def test_wiring_cost_and_mean():
    edges = [(1, 2), (1, 3)]
    positions = {1: (0.0, 0.0), 2: (1.0, 0.0), 3: (3.0, 0.0)}
    assert wiring_cost(edges, positions) == 4.0
    assert mean_edge_length(edges, positions) == 2.0

def test_communication_cost_is_event_plus_distance():
    edges = [(1, 2), (1, 3)]
    positions = {1: (0.0, 0.0), 2: (1.0, 0.0), 3: (3.0, 0.0)}
    assert communication_cost(edges, positions) == 6.0
    assert cost_per_edge(edges, positions) == 3.0

def test_communication_cost_without_positions():
    assert communication_cost([(1, 2), (2, 3)]) == 2.0
