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
        "pre_root_id,post_root_id,syn_count\n"
        "a,b,4\n"
        "a,c,5\n"
        "b,c,10\n"
    )
    assert load_edges(p, min_synapses=5) == {("a", "c"), ("b", "c")}


def test_rich_club_loader_aggregates_synapses_across_region_rows(tmp_path):
    """Pair-level threshold: rows for the same directed pair must be summed
    before applying the minimum-synapse cutoff (Codex / Lin et al. definition).
    """
    p = tmp_path / "connections.csv"
    p.write_text(
        "pre_root_id,post_root_id,syn_count,neuropil\n"
        "a,b,4,ME\n"
        "a,b,2,LO\n"
        "a,c,3,ME\n"
        "b,c,10,LO\n"
    )
    # a->b totals 6 (>=5) so it must be kept; a->c totals 3 (<5) so it is dropped
    assert load_edges(p, min_synapses=5) == {("a", "b"), ("b", "c")}



def test_rich_club_curve_matches_direct_definition_on_multiple_thresholds():
    edges = {
        ("a", "b"), ("b", "a"), ("a", "c"), ("c", "a"), ("b", "c"),
        ("c", "d"), ("d", "c"), ("d", "a")
    }
    thresholds = [1, 2, 3, 4, 5]
    rows = curve(edges, thresholds)
    indeg = {}
    outdeg = {}
    for u, v in edges:
        outdeg[u] = outdeg.get(u, 0) + 1
        indeg[v] = indeg.get(v, 0) + 1
    degree = {u: indeg.get(u, 0) + outdeg.get(u, 0) for u in set(indeg) | set(outdeg)}
    expected = []
    for k in sorted(set(thresholds)):
        rich = {u for u, d in degree.items() if d >= k}
        possible = len(rich) * (len(rich) - 1)
        re = sum(1 for u, v in edges if u in rich and v in rich)
        cross = sum(1 for u, v in edges if (u in rich) ^ (v in rich))
        expected.append((k, len(rich), re, re / possible if possible else 0.0, cross / len(edges)))
    actual = [(r["threshold"], r["rich_nodes"], r["rich_edges"], r["rich_density"], r["cross_fraction"]) for r in rows]
    assert actual == expected
