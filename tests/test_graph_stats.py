from pathlib import Path
from src.graph.stats import degree_statistics

def test_degree_statistics_deduplicates_region_rows(tmp_path: Path):
    p=tmp_path/"x.csv"
    p.write_text("pre_root_id,post_root_id,neuropil,syn_count\nA,B,ME,3\nA,B,LO,4\nB,A,ME,2\n",encoding="utf-8")
    r=degree_statistics(p)
    assert r["unique_directed_pairs"]==2
    assert r["in_degree"]["mean"]==1.0
    assert r["out_degree"]["mean"]==1.0
