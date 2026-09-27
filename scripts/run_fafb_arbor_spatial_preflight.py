#!/usr/bin/env python3
"""FAFB v783 arbor-aware spatial preflight for Gate C.

Uses synapse-level pre/post coordinates to build outgoing/incoming centroid
proxies per neuron. This follows the source-outgoing -> target-incoming
distance concept used in Lin et al. (2024), but the result remains a
synapse-derived arbor proxy, not an axon-length measurement.

No spatial null or scientific conclusion is produced here.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

from src.graph.connections import aggregate_pair_synapses


ALIASES = {
    "pre_root": ["pre_root_id", "pre_pt_root_id", "pre"],
    "post_root": ["post_root_id", "post_pt_root_id", "post"],
    "x": ["x", "syn_x"],
    "y": ["y", "syn_y"],
    "z": ["z", "syn_z"],
    "pre_position": ["pre_pt_position", "pre_position"],
    "post_position": ["post_pt_position", "post_position"],
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pick(fieldnames, names):
    for name in names:
        if name in fieldnames:
            return name
    return None


def parse_position(raw: str):
    s = str(raw).strip().strip("[]()")
    parts = s.replace(",", " ").split()
    if len(parts) != 3:
        raise ValueError(f"invalid 3D position: {raw!r}")
    return tuple(float(x) for x in parts)


def resolve_schema(fieldnames):
    f = set(fieldnames or [])
    pre_root = pick(f, ALIASES["pre_root"])
    post_root = pick(f, ALIASES["post_root"])
    xyz = all(pick(f, ALIASES[k]) for k in ("x", "y", "z"))
    paired = pick(f, ALIASES["pre_position"]) and pick(f, ALIASES["post_position"])
    if not pre_root or not post_root or not (xyz or paired):
        raise ValueError(
            "Unsupported synapse-coordinate schema. Required pre/post root IDs "
            "plus either pre/post XYZ columns or pre/post position columns. "
            f"Observed columns: {list(fieldnames or [])}"
        )
    return {
        "pre_root": pre_root,
        "post_root": post_root,
        "mode": "synapse_xyz" if xyz else "position",
        "x": pick(f, ALIASES["x"]), "y": pick(f, ALIASES["y"]), "z": pick(f, ALIASES["z"]),
        "pre_position": pick(f, ALIASES["pre_position"]), "post_position": pick(f, ALIASES["post_position"]),
    }


def add_point(acc, rid, point):
    s = acc[rid]
    s[0] += point[0]
    s[1] += point[1]
    s[2] += point[2]
    s[3] += 1


def load_arbor_centroids(path: Path):
    outgoing = defaultdict(lambda: [0.0, 0.0, 0.0, 0])
    incoming = defaultdict(lambda: [0.0, 0.0, 0.0, 0])
    rows = 0
    malformed = 0
    schema = None

    with gzip.open(path, "rt", newline="") as fh:
        reader = csv.DictReader(fh)
        columns = list(reader.fieldnames or [])
        schema = resolve_schema(columns)
        current_pre = None
        current_post = None
        for row in reader:
            rows += 1
            try:
                if row[schema["pre_root"]].strip(): current_pre = row[schema["pre_root"]].strip()
                if row[schema["post_root"]].strip(): current_post = row[schema["post_root"]].strip()
                if not current_pre or not current_post: raise ValueError("coordinate row precedes pair header")
                if schema["mode"] == "synapse_xyz":
                    point = tuple(float(row[schema[k]]) for k in ("x","y","z"))
                    add_point(outgoing, current_pre, point)
                    add_point(incoming, current_post, point)
                else:
                    add_point(outgoing, current_pre, parse_position(row[schema["pre_position"]]))
                    add_point(incoming, current_post, parse_position(row[schema["post_position"]]))
            except (KeyError, TypeError, ValueError):
                malformed += 1

    out_centroids = {
        rid: (v[0] / v[3], v[1] / v[3], v[2] / v[3])
        for rid, v in outgoing.items() if v[3]
    }
    in_centroids = {
        rid: (v[0] / v[3], v[1] / v[3], v[2] / v[3])
        for rid, v in incoming.items() if v[3]
    }
    return schema, columns, rows, malformed, outgoing, incoming, out_centroids, in_centroids


def distance(a, b):
    dx = (a[0] - b[0]) * 4.0
    dy = (a[1] - b[1]) * 4.0
    dz = (a[2] - b[2]) * 40.0
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def quantiles(values):
    if not values:
        return {}
    xs = sorted(values)

    def q(p):
        return xs[min(len(xs) - 1, max(0, int(round(p * (len(xs) - 1)))))]

    return {
        "min_nm": xs[0],
        "q25_nm": q(0.25),
        "median_nm": q(0.50),
        "q75_nm": q(0.75),
        "q90_nm": q(0.90),
        "q95_nm": q(0.95),
        "q99_nm": q(0.99),
        "max_nm": xs[-1],
        "mean_nm": sum(xs) / len(xs),
    }


def histogram(values, bins):
    out = Counter()
    for x in values:
        for i in range(len(bins) - 1):
            if bins[i] <= x < bins[i + 1]:
                out[i] += 1
                break
        else:
            if x == bins[-1]:
                out[len(bins) - 2] += 1
    return {f"{bins[i]}-{bins[i+1]}": out.get(i, 0) for i in range(len(bins) - 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--connections", default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--synapse-coordinates", default="data/raw/fafb_v783/synapse_coordinates.csv.gz")
    ap.add_argument("--output", default="artifacts/fafb-v783/arbor-spatial-preflight.json")
    ap.add_argument("--min-synapses", type=int, default=5)
    ap.add_argument("--edge-sample", type=int, default=100000)
    ap.add_argument("--nonedge-sample", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260927)
    args = ap.parse_args()

    cpath = Path(args.synapse_coordinates)
    epath = Path(args.connections)

    schema, columns, syn_rows, malformed, outgoing_raw, incoming_raw, out_centroids, in_centroids = load_arbor_centroids(cpath)
    edges = aggregate_pair_synapses(epath, min_synapses=args.min_synapses)
    graph_nodes = {u for u, _ in edges} | {v for _, v in edges}
    degree = Counter()
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    out_covered = graph_nodes & out_centroids.keys()
    in_covered = graph_nodes & in_centroids.keys()
    both_covered = out_covered & in_covered

    rng = random.Random(args.seed)
    edge_sample = rng.sample(list(edges.keys()), min(args.edge_sample, len(edges)))
    edge_distances = [
        distance(out_centroids[u], in_centroids[v])
        for u, v in edge_sample
        if u in out_centroids and v in in_centroids
    ]

    edge_set = set(edges.keys())
    nodes = list(graph_nodes)
    nonedges = []
    nonedge_set = set()
    attempts = 0
    max_attempts = max(1000, args.nonedge_sample * 50)
    target_nonedges = min(
        args.nonedge_sample,
        len(nodes) * max(0, len(nodes) - 1) - len(edges),
    )
    while len(nonedges) < target_nonedges and attempts < max_attempts:
        attempts += 1
        u, v = rng.sample(nodes, 2)
        pair = (u, v)
        if pair in edge_set or pair in nonedge_set:
            continue
        nonedge_set.add(pair)
        nonedges.append(pair)

    nonedge_distances = [
        distance(out_centroids[u], in_centroids[v])
        for u, v in nonedges
        if u in out_centroids and v in in_centroids
    ]

    bins = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
    covered_degree = [degree[n] for n in both_covered]
    missing_degree = [degree[n] for n in graph_nodes - both_covered]
    degree_coverage = {}
    for lo, hi in [(0,9),(10,19),(20,36),(37,74),(75,92),(93,149),(150,999999)]:
        total = sum(1 for n in graph_nodes if lo <= degree[n] <= hi)
        covered = sum(1 for n in both_covered if lo <= degree[n] <= hi)
        degree_coverage[f"{lo}-{hi}"] = {"nodes": total, "both_centroid_nodes": covered, "coverage": covered/total if total else None}
    result = {
        "dataset": "FAFB",
        "version": "v783",
        "purpose": "Gate C0 arbor-aware spatial preflight; no spatial null or scientific conclusion",
        "inputs": {
            "connections": str(epath),
            "connections_sha256": sha256(epath),
            "synapse_coordinates": str(cpath),
            "synapse_coordinates_sha256": sha256(cpath),
            "min_synapses": args.min_synapses,
        },
        "synapse_coordinate_schema": {
            "observed_columns": columns,
            "resolved_fields": schema,
            "coordinate_units": "FAFB voxel coordinates",
            "voxel_size_nm": [4, 4, 40],
            "row_semantics": "one synapse-level pre/post coordinate record as supplied by the source file",
        },
        "synapse_inventory": {
            "rows": syn_rows,
            "malformed_rows": malformed,
            "outgoing_root_ids": len(outgoing_raw),
            "incoming_root_ids": len(incoming_raw),
            "outgoing_centroid_nodes": len(out_centroids),
            "incoming_centroid_nodes": len(in_centroids),
        },
        "graph_inventory": {
            "unique_directed_pairs": len(edges),
            "graph_nodes": len(graph_nodes),
            "nodes_with_outgoing_centroids": len(out_covered),
            "nodes_with_incoming_centroids": len(in_covered),
            "nodes_with_both_centroids": len(both_covered),
            "outgoing_centroid_coverage": len(out_covered) / len(graph_nodes) if graph_nodes else 0.0,
            "incoming_centroid_coverage": len(in_covered) / len(graph_nodes) if graph_nodes else 0.0,
            "both_centroid_coverage": len(both_covered) / len(graph_nodes) if graph_nodes else 0.0,
            "both_centroid_degree_summary": {"covered_median_degree": median(covered_degree) if covered_degree else None, "missing_median_degree": median(missing_degree) if missing_degree else None, "covered_max_degree": max(covered_degree) if covered_degree else None, "missing_max_degree": max(missing_degree) if missing_degree else None},
            "both_centroid_coverage_by_total_degree": degree_coverage,
        },
        "centroid_semantics": {
            "source_position": "mean of outgoing synapse pre-site coordinates",
            "target_position": "mean of incoming synapse post-site coordinates",
            "distance": "anisotropic Euclidean distance between source outgoing centroid and target incoming centroid, in nm",
            "interpretation": "synapse-derived arbor proxy; not axon length, dendrite length, or soma distance",
        },
        "sampling": {
            "seed": args.seed,
            "requested_edge_sample": args.edge_sample,
            "accepted_edge_sample": len(edge_distances),
            "requested_nonedge_sample": args.nonedge_sample,
            "candidate_nonedges_generated": len(nonedges),
            "accepted_nonedge_distance_sample": len(nonedge_distances),
            "nonedge_sampling_attempts": attempts,
        },
        "distance_summary": {
            "observed_edges_nm": quantiles(edge_distances),
            "sampled_nonedges_nm": quantiles(nonedge_distances),
            "observed_edge_histogram_nm": histogram(edge_distances, bins),
            "sampled_nonedge_histogram_nm": histogram(nonedge_distances, bins),
        },
        "next_gate": {
            "C1": "degree-preserving spatial rewiring only after distance definition and coverage are validated",
            "C2": "NPC + spatial sensitivity only after C1 is validated and computationally tractable",
            "C3": "EDR/projectome sensitivity; not a neuron-level NPC replacement",
        },
        "missing_coordinate_policy": "pairs missing either required centroid are excluded from distance summaries and reported through coverage metrics",
        "scientific_conclusion": None,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
