from scripts.run_c2_positive_control import (
    build_base_graph, constraint_signature, degree_maps,
    plant_rich_club, club_edge_count, run_null,
)

def test_planted_signal_preserves_c2_signature():
    base, blocks = build_base_graph(50, 0.16, 1)
    _, _, degrees = degree_maps(base)
    club = set(sorted(degrees, key=lambda u: (degrees[u], u), reverse=True)[:8])
    planted = set(base)
    plant_rich_club(planted, blocks, club, 20, 7, 200000)
    assert constraint_signature(base, blocks) == constraint_signature(planted, blocks)
    assert club_edge_count(planted, club) > club_edge_count(base, club)

def test_unbiased_null_reduces_planted_fixed_club_signal():
    base, blocks = build_base_graph(80, 0.18, 1)
    _, _, degrees = degree_maps(base)
    club = set(sorted(degrees, key=lambda u: (degrees[u], u), reverse=True)[:12])
    planted = set(base)
    plant_rich_club(planted, blocks, club, 50, 7, 500000)
    planted_count = club_edge_count(planted, club)
    null, accepted, null_count = run_null(planted, blocks, club, 100000, 101)
    assert accepted > 0
    assert constraint_signature(planted, blocks) == constraint_signature(null, blocks)
    assert null_count < planted_count
