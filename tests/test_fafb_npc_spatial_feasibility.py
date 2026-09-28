from scripts.run_fafb_npc_spatial_feasibility import block_counts

def test_block_counts_freezes_edges_without_block_assignments():
    edges={("a","c"),("a","d"),("x","c")}
    blocks={"a":"X","c":"Y"}
    assert block_counts(edges,blocks)=={("X","Y"):1}
