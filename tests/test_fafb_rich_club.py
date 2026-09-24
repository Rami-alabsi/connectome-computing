from scripts.run_fafb_rich_club import curve


def test_rich_club_curve_uses_explicit_directed_thresholds():
    edges = {
        ("a", "b"), ("b", "a"), ("a", "c"), ("c", "a"), ("b", "c")
    }
    rows = curve(edges, [2, 3])
    assert [r["threshold"] for r in rows] == [2, 3]
    assert rows[0]["rich_nodes"] == 3
    assert rows[0]["rich_edges"] == 5
    assert rows[0]["rich_density"] == 5 / 6
