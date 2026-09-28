from scripts.run_fafb_npc_spatial_feasibility import (
    block_counts,
    build_block_buckets,
    choose_bucket_pair,
)


def test_block_counts_freezes_edges_without_block_assignments():
    edges={("a","c"),("a","d"),("x","c")}
    blocks={"a":"X","c":"Y"}
    assert block_counts(edges,blocks)=={("X","Y"):1}


def test_block_pair_stratified_proposal_stays_in_same_block_class():
    edges=[("a","c"),("b","d"),("a","d"),("b","c"),("x","c")]
    blocks={"a":"X","b":"X","c":"Y","d":"Y"}
    buckets,keys,cumulative,total=build_block_buckets(edges,blocks)
    assert len(buckets)==1
    assert keys==[("X","Y")]
    assert total==6
    i,j=choose_bucket_pair(__import__("random").Random(7),buckets,keys,cumulative,total)
    assert (blocks[edges[i][0]],blocks[edges[i][1]])==("X","Y")
    assert (blocks[edges[j][0]],blocks[edges[j][1]])==("X","Y")
