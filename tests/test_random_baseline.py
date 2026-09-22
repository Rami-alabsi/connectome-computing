from src.graph.random_baseline import degree_preserving_randomization

def degrees(edges):
    indegree = {}
    outdegree = {}
    for u, v in edges:
        outdegree[u] = outdegree.get(u, 0) + 1
        indegree[v] = indegree.get(v, 0) + 1
    return indegree, outdegree

def test_degree_sequences_are_preserved():
    edges = {
        ("a", "b"), ("a", "c"),
        ("b", "c"), ("b", "d"),
        ("c", "a"), ("d", "a"),
    }
    randomized = degree_preserving_randomization(edges, swaps=100, seed=42)
    assert degrees(randomized) == degrees(edges)
    assert all(u != v for u, v in randomized)
    assert len(randomized) == len(edges)
