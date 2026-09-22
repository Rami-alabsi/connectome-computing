from src.generator.capacity import build_capacity_hierarchy, capacity_hierarchy_graph


def test_capacity_saturation_creates_peer_modules():
    h = build_capacity_hierarchy(10, module_capacity=3, hierarchy_depth=2)
    assert len(h.module_nodes) == 4
    assert [len(x) for x in h.module_nodes] == [3, 3, 3, 1]
    assert max(map(len, h.module_nodes)) <= 3


def test_capacity_hierarchy_is_deterministic():
    a = build_capacity_hierarchy(25, module_capacity=4, hierarchy_depth=3)
    b = build_capacity_hierarchy(25, module_capacity=4, hierarchy_depth=3)
    assert a == b


def test_capacity_graph_is_seed_deterministic():
    e1, h1 = capacity_hierarchy_graph(
        30, 120, module_capacity=5, interface_budget=2, seed=11
    )
    e2, h2 = capacity_hierarchy_graph(
        30, 120, module_capacity=5, interface_budget=2, seed=11
    )
    assert e1 == e2
    assert h1 == h2


def test_capacity_graph_respects_simple_graph_and_local_capacity():
    edges, h = capacity_hierarchy_graph(
        24, 80, module_capacity=4, interface_budget=3, seed=5
    )
    assert len(edges) == 80
    assert all(u != v for u, v in edges)
    assert max(map(len, h.module_nodes)) <= 4
