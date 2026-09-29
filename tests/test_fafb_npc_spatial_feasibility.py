

def test_c2_resume_matches_uninterrupted_trajectory(tmp_path, monkeypatch):
    """A checkpoint/resume run must reproduce the same final state as uninterrupted C2."""
    import csv
    import gzip
    import sys

    from scripts.run_fafb_npc_spatial_feasibility import load_c2_state, main

    connections = tmp_path / "connections.csv"
    with connections.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["pre_root_id", "post_root_id", "syn_count", "neuropil"])
        nodes = ("a", "b", "c", "d", "e", "f")
        for source in nodes:
            for target in nodes:
                if source != target:
                    writer.writerow([source, target, 5, "X"])

    centroids = tmp_path / "centroids.csv.gz"
    with gzip.open(centroids, "wt", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["root_id", "out_x", "out_y", "out_z", "in_x", "in_y", "in_z"])
        for node in ("a", "b", "c", "d", "e", "f"):
            writer.writerow([node, 0, 0, 0, 0, 0, 0])

    def run(output, attempts, resume_state=""):
        argv = [
            "c2", "--connections", str(connections), "--centroids", str(centroids),
            "--output", str(output), "--seed", "20260935", "--attempts", str(attempts),
            "--target-accepted", "0", "--min-synapses", "5", "--checkpoint-every", "100",
            "--code-version", "sampler-test",
        ]
        if resume_state:
            argv += ["--resume-state", str(resume_state)]
        monkeypatch.setattr(sys, "argv", argv)
        main()

    first = tmp_path / "first.json"
    run(first, 100)
    checkpoint = tmp_path / "resume-state.pkl.gz"
    checkpoint.write_bytes((tmp_path / "c2-state.pkl.gz").read_bytes())

    resumed = tmp_path / "resumed.json"
    run(resumed, 200, checkpoint)
    resumed_state = load_c2_state(tmp_path / "c2-state.pkl.gz")

    isolated = tmp_path / "isolated"
    isolated.mkdir()
    isolated_connections = isolated / "connections.csv"
    isolated_connections.write_bytes(connections.read_bytes())
    isolated_centroids = isolated / "centroids.csv.gz"
    isolated_centroids.write_bytes(centroids.read_bytes())
    monkeypatch.setattr(sys, "argv", [
        "c2", "--connections", str(isolated_connections), "--centroids", str(isolated_centroids),
        "--output", str(isolated / "uninterrupted.json"), "--seed", "20260935",
        "--attempts", "200", "--target-accepted", "0", "--min-synapses", "5",
        "--checkpoint-every", "100", "--code-version", "sampler-test",
    ])
    main()
    uninterrupted_state = load_c2_state(isolated / "c2-state.pkl.gz")

    assert resumed_state["attempt"] == uninterrupted_state["attempt"] == 200
    assert resumed_state["accepted"] == uninterrupted_state["accepted"]
    assert resumed_state["invalid"] == uninterrupted_state["invalid"]
    assert resumed_state["block_reject"] == uninterrupted_state["block_reject"]
    assert resumed_state["distance_reject"] == uninterrupted_state["distance_reject"]
    assert resumed_state["edge_list"] == uninterrupted_state["edge_list"]
    assert resumed_state["edge_bins"] == uninterrupted_state["edge_bins"]
    assert resumed_state["rng_state"] == uninterrupted_state["rng_state"]
