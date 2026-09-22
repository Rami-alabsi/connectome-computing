from pathlib import Path
from src.graph.stats import degree_statistics

def test_degree_and_reciprocity(tmp_path: Path) -> None:
    p = tmp_path / "connections.csv"
    p.write_text(
        "pre_root_id,post_root_id,syn_count\n"
        "1,2,3\n"
        "2,1,4\n"
        "2,3,2\n",
        encoding="utf-8",
    )
    result = degree_statistics(p)
    assert result["nodes"] == 3
    assert result["unique_directed_pairs"] == 3
    assert result["in_degree"]["max"] == 1
    assert result["out_degree"]["max"] == 2
    assert result["reciprocal_pair_fraction"] == 2 / 3
    assert result["weighted_synapse_total"] == 9
