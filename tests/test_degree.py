from src.graph.degree import degree_profile

def test_degree_profile_captures_directional_hubs():
    edges = {
        ("a", "b"), ("a", "c"), ("a", "d"),
        ("b", "a"), ("c", "a"), ("d", "a"),
        ("a", "e"), ("a", "f"),
    }
    result = degree_profile(edges, hub_multiplier=2.0)
    assert result.nodes == 6
    assert result.directed_edges == 8
    assert result.max_out == 5
    assert result.max_in == 3
    assert result.hub_fraction_in > 0
    assert result.hub_fraction_out > 0

def test_degree_profile_includes_declared_isolated_nodes():
    result = degree_profile({("a", "b")}, nodes=["a", "b", "c"])
    assert result.nodes == 3
    assert result.mean_in == result.mean_out == 1 / 3
    assert result.max_in == 1
    assert result.max_out == 1
