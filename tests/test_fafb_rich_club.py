from scripts.run_fafb_rich_club import curve, load_edges


def test_rich_club_curve_uses_explicit_directed_thresholds():
    edges = {
        ("a", "b"), ("b", "a"), ("a", "c"), ("c", "a"), ("b", "c")
    }
    rows = curve(edges, [2, 3])
    assert [r["threshold"] for r in rows] == [2, 3]
    assert rows[0]["rich_nodes"] == 3
    assert rows[0]["rich_edges"] == 5
    assert rows[0]["rich_density"] == 5 / 6


def test_rich_club_loader_applies_synapse_threshold(tmp_path):
    p = tmp_path / "connections.csv"
    p.write_text(
        "pre_root_id,post_root_id,syn_count\\n"
        "a,b,4\\n"
        "a,c,5\\n"
        "b,c,10\\n"
    )
    assert load_edges(p, min_synapses=5) == {("a", "c"), ("b", "c")}
