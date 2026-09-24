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


def test_npc_loader_aggregates_pair_rows_before_threshold(tmp_path):
    import csv
    import gzip
    from scripts.run_fafb_npc_rich_club import load_graph

    path=tmp_path / "connections.csv.gz"
    rows=[
        ["pre_root_id","post_root_id","syn_count","neuropil"],
        ["1","2","3","AL(R)"],
        ["1","2","3","MB(R)"],
        ["1","3","4","AL(R)"],
        ["2","3","5","MB(R)"],
    ]
    with gzip.open(path,"wt",newline="",encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)

    edges,blocks=load_graph(path,min_synapses=5)
    assert edges=={("1","2"),("2","3")}
    assert blocks["1"]=="AL(R)"
    assert blocks["2"]=="MB(R)"
    assert "3" not in blocks
