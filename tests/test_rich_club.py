from src.graph.rich_club import rich_club_profile

def test_rich_club_profile_counts_core_edges():
    result=rich_club_profile({("a","b"),("b","a"),("a","c"),("c","a"),("b","c")},degree_threshold=3)
    assert result.rich_nodes==3
    assert result.rich_edge_count==5
    assert result.rich_density>0

def test_rich_club_keeps_declared_isolates():
    result=rich_club_profile({("a","b")},nodes=["a","b","c"],degree_threshold=1)
    assert result.nodes==3
    assert result.rich_nodes==2
