from src.graph.rich_club import rich_club_curve, rich_club_profile

def test_rich_club_profile_counts_core_edges():
    result = rich_club_profile(
        {("a","b"),("b","a"),("a","c"),("c","a"),("b","c")},
        degree_threshold=3,
    )
    assert result.rich_nodes == 3
    assert result.rich_edge_count == 5
    assert result.rich_density > 0

def test_rich_club_keeps_declared_isolates():
    result = rich_club_profile({("a","b")}, nodes=["a","b","c"], degree_threshold=1)
    assert result.nodes == 3
    assert result.rich_nodes == 2

def test_rich_club_curve_has_multiple_thresholds():
    curve = rich_club_curve({("a","b"),("b","c"),("c","a"),("a","d")}, thresholds=[1,2,3])
    assert [p.threshold for p in curve] == [1,2,3]
    assert len(curve) == 3
