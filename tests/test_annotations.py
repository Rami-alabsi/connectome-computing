from pathlib import Path
from src.graph.annotations import build_annotation_index, summarize_annotations

def test_annotation_summary_and_index(tmp_path: Path):
    path = tmp_path / "annotations.csv"
    path.write_text("root_id,cell_type,neuropil,neurotransmitter\n1,T1,AL,GABA\n2,T2,MB,Glutamate\n1,T1,AL,GABA\n", encoding="utf-8")
    summary = summarize_annotations(path)
    assert summary["unique_neurons"] == 2
    assert summary["selected_columns"]["cell_type"] == "cell_type"
    index = build_annotation_index(path)
    assert index["1"]["cell_type"] == "T1"
    assert index["2"]["neuropil"] == "MB"
