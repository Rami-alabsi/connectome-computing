from src.graph.random_baseline import degree_preservation_report
from scripts.run_fafb_motif_sample import signature

def test_signature_has_six_directed_bits():
    edges={("a","b"),("b","c")}
    s=signature("a","b","c",edges)
    assert isinstance(s,int)
    assert 0 <= s < 64

def test_degree_report_exact():
    e={("a","b"),("b","c"),("c","a")}
    assert degree_preservation_report(e,set(e)) == {
        "same_edge_count":True,"same_in_degree":True,"same_out_degree":True}


def test_canonical_triad_classes_cover_all_16_labels():
    from scripts.run_fafb_motif_sample import TRIAD_REPRESENTATIVES, canonical_triad_class
    for label, pairs in TRIAD_REPRESENTATIVES.items():
        edges = {(str(u), str(v)) for u, v in pairs}
        assert canonical_triad_class("0", "1", "2", edges) == label
