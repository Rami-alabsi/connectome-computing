from scripts.run_fafb_npc_spatial_feasibility import (
    block_counts,
    build_block_buckets,
    choose_bucket_pair,
    c2_rich_club_curve,
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


def test_c2_rich_club_curve_reports_single_null_descriptively():
    edges = {("a","b"),("a","c"),("b","a"),("b","c"),("c","a"),("c","b")}
    result = c2_rich_club_curve(edges, edges, thresholds=[2,3])
    assert result["null_count"] == 1
    assert result["interpretation"].startswith("descriptive single-null")
    assert all(row["phi_norm"] == 1.0 for row in result["curve"])


def test_c2_checkpoint_roundtrip_preserves_rng_and_state(tmp_path):
    import random
    from scripts.run_fafb_npc_spatial_feasibility import load_c2_state, save_c2_state

    rng=random.Random(20260935)
    for _ in range(17):
        rng.random()
    state={
        "version":1,
        "seed":20260935,
        "code_version":"sampler-test",
        "attempt":170,
        "accepted":11,
        "invalid":7,
        "block_reject":0,
        "distance_reject":152,
        "edge_list":[("a","b"),("b","c")],
        "edge_bins":[1,2],
        "rng_state":rng.getstate(),
        "checkpoints":[{"attempts":170,"accepted_swaps":11}],
    }
    path=tmp_path/"c2-state.pkl.gz"
    save_c2_state(path,state)
    restored=load_c2_state(path)
    assert restored==state

    rng2=random.Random()
    rng2.setstate(restored["rng_state"])
    assert [rng.random() for _ in range(10)] == [rng2.random() for _ in range(10)]
