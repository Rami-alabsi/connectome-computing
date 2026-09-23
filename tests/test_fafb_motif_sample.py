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
