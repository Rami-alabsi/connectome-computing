from pathlib import Path
from src.graph.connections import summarize

def test_summarize_connection_fixture(tmp_path: Path) -> None:
    p = tmp_path / "connections.csv"
    p.write_text(
        "pre_root_id,post_root_id,syn_count,region\n"
        "1,2,3,AL\n"
        "1,2,4,MB\n"
        "2,3,2,AL\n",
        encoding="utf-8",
    )
    result = summarize(p)
    assert result["nodes"] == 3
    assert result["edge_rows"] == 3
    assert result["unique_directed_pairs"] == 2
    assert result["multi_region_pair_rows"] == 1
    assert result["total_synapses"] == 9
