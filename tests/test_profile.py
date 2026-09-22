from pathlib import Path
from src.generator.profile import StructuralProfile, load_profile, profile_from_edges, save_profile


def test_profile_from_edges():
    edges = {("a", "b"), ("b", "a"), ("a", "c")}
    profile = profile_from_edges(edges)
    assert profile.nodes == 3
    assert profile.directed_edges == 3
    assert profile.mean_out_degree == 1.0
    assert profile.mean_in_degree == 1.0
    assert profile.reciprocal_edge_fraction == 2 / 3
    assert profile.max_out_degree == 2
    assert profile.max_in_degree == 1


def test_profile_preserves_declared_isolate():
    profile = profile_from_edges({("a", "b")}, node_ids={"a", "b", "c"})
    assert profile.nodes == 3
    assert profile.median_in_degree == 0
    assert profile.median_out_degree == 0


def test_profile_round_trip(tmp_path: Path):
    profile = StructuralProfile(100, 200, 200/(100*99), 2.0, 2.0, 0.1)
    path = tmp_path / "profile.json"
    save_profile(profile, path)
    assert load_profile(path) == profile
