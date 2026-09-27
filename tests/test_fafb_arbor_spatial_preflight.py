from pathlib import Path
import gzip
import json

from scripts.run_fafb_arbor_spatial_preflight import load_arbor_centroids, resolve_schema


def test_resolve_synapse_coordinate_xyz_schema():
    fields = [
        "pre_pt_root_id", "post_pt_root_id",
        "pre_x", "pre_y", "pre_z", "post_x", "post_y", "post_z",
    ]
    schema = resolve_schema(fields)
    assert schema["mode"] == "xyz"
    assert schema["pre_root"] == "pre_pt_root_id"
    assert schema["post_root"] == "post_pt_root_id"


def test_resolve_synapse_coordinate_position_schema(tmp_path):
    path = tmp_path / "syn.csv.gz"
    raw = (
        "pre_root_id,post_root_id,pre_pt_position,post_pt_position\n"
        "1,2,[1 2 3],[4 5 6]\n"
        "1,2,[3 4 5],[6 7 8]\n"
    )
    with gzip.open(path, "wt", newline="") as fh:
        fh.write(raw)

    schema, rows, malformed, outgoing, incoming, out_centroids, in_centroids = load_arbor_centroids(path)
    assert schema["mode"] == "position"
    assert rows == 2
    assert malformed == 0
    assert out_centroids["1"] == (2.0, 3.0, 4.0)
    assert in_centroids["2"] == (5.0, 6.0, 7.0)
