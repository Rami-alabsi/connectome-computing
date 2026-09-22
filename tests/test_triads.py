from src.graph.triads import classify_triad, canonical_signature

def test_empty_triad():
    assert classify_triad(("a", "b", "c"), set()) == "empty"

def test_single_edge():
    assert classify_triad(("a", "b", "c"), {("a", "b")}) == "single_edge"

def test_reciprocal_pair():
    assert classify_triad(("a", "b", "c"), {("a", "b"), ("b", "a")}) == "single_reciprocal_pair"

def test_three_edge_cycle():
    edges = {("a", "b"), ("b", "c"), ("c", "a")}
    assert classify_triad(("a", "b", "c"), edges) == "three_edge_directed_triad"

def test_signature_is_order_invariant():
    edges = {("a", "b"), ("b", "c"), ("a", "c")}
    assert canonical_signature(("a", "b", "c"), edges) == canonical_signature(("c", "a", "b"), edges)
