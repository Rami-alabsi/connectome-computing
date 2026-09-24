from collections import Counter
from scripts.run_fafb_npc_rich_club import constrained_randomization, degree_report, block_counts

def test_npc_swap_preserves_degree_and_blocks():
    edges={
        ("a","c"),("a","d"),("b","c"),("b","d"),
        ("c","a"),("d","b")
    }
    blocks={"a":"X","b":"X","c":"Y","d":"Y"}
    null, successful, attempts = constrained_randomization(edges, blocks, 20, 7)
    assert successful > 0
    assert attempts >= successful
    rep=degree_report(edges,null)
    assert rep["same_edge_count"]
    assert rep["same_in_degree"]
    assert rep["same_out_degree"]
    assert block_counts(edges,blocks)==block_counts(null,blocks)
