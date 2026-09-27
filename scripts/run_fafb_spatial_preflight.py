#!/usr/bin/env python3
"""FAFB v783 spatial-data preflight for Gate C.

This is an inventory/diagnostic step only. It does not generate a spatial null
and does not make a Gate C scientific conclusion.
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
from statistics import median
from pathlib import Path

from src.graph.connections import aggregate_pair_synapses


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_coordinates(path: Path):
    positions = defaultdict(list)
    rows = 0
    with gzip.open(path, "rt", newline="") as fh:
        reader = csv.DictReader(fh)
        required = {"root_id", "position"}
        if not required.issubset(reader.fieldnames or set()):
            raise ValueError(f"coordinates file must contain {sorted(required)}")
        for row in reader:
            rows += 1
            rid = row["root_id"]
            raw = row["position"].strip().strip("[]")
            parts = raw.split()
            if len(parts) != 3:
                raise ValueError(f"invalid position for root_id={rid}: {row['position']}")
            positions[rid].append(tuple(float(x) for x in parts))

    # A root_id can have multiple stable point/supervoxel positions. The raw
    # coordinates file therefore cannot be treated as a one-row-per-neuron
    # table. Use a deterministic component-wise median as the first-pass
    # neuron-position proxy; this is NOT a soma coordinate.
    coords = {
        rid: tuple(median(axis) for axis in zip(*points))
        for rid, points in positions.items()
    }
    multiplicities = [len(points) for points in positions.values()]
    duplicate_rows = rows - len(positions)
    return coords, rows, duplicate_rows, multiplicities


def distance(a, b):
    # FAFB coordinates are voxel indices with anisotropic voxel size.
    dx = (a[0] - b[0]) * 4.0
    dy = (a[1] - b[1]) * 4.0
    dz = (a[2] - b[2]) * 40.0
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def quantiles(values):
    if not values:
        return {}
    xs = sorted(values)
    def q(p):
        idx = min(len(xs) - 1, max(0, int(round(p * (len(xs) - 1)))))
        return xs[idx]
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
    ap.add_argument("--coordinates", default="data/raw/fafb_v783/coordinates.csv.gz")
    ap.add_argument("--output", default="artifacts/fafb-v783/spatial-preflight.json")
    ap.add_argument("--min-synapses", type=int, default=5)
    ap.add_argument("--edge-sample", type=int, default=100000)
    ap.add_argument("--nonedge-sample", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260927)
    args = ap.parse_args()

    cpath = Path(args.coordinates)
    epath = Path(args.connections)
    coords, coordinate_rows, duplicate_rows, coordinate_multiplicities = load_coordinates(cpath)

    edges = aggregate_pair_synapses(epath, min_synapses=args.min_synapses)
    graph_nodes = {u for u, _ in edges} | {v for _, v in edges}
    covered_nodes = graph_nodes & coords.keys()

    rng = random.Random(args.seed)
    edge_sample = rng.sample(list(edges.keys()), min(args.edge_sample, len(edges)))
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

    edge_distances = [
        distance(coords[u], coords[v])
        for u, v in edge_sample
        if u in coords and v in coords
    ]
    nonedge_distances = [
        distance(coords[u], coords[v])
        for u, v in nonedges
        if u in coords and v in coords
    ]

    bins = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
    result = {
        "dataset": "FAFB",
        "version": "v783",
        "purpose": "Gate C spatial preflight; no spatial null or scientific conclusion",
        "inputs": {
            "connections": str(epath),
            "connections_sha256": sha256(epath),
            "coordinates": str(cpath),
            "coordinates_sha256": sha256(cpath),
            "min_synapses": args.min_synapses,
        },
        "coordinate_schema": {
            "columns": ["root_id", "position", "supervoxel_id"],
            "position_units": "FAFB voxel coordinates",
            "voxel_size_nm": [4, 4, 40],
            "distance_metric": "anisotropic Euclidean distance in nm",
            "position_reduction": "component-wise median across all positions for each root_id",
            "position_semantics": "supervoxel/stable-point position proxy; not a soma coordinate",
        },
        "coordinate_inventory": {
            "rows": coordinate_rows,
            "unique_root_ids": len(coords),
            "duplicate_rows_collapsed": duplicate_rows,
            "roots_with_multiple_positions": sum(n > 1 for n in coordinate_multiplicities),
            "max_positions_per_root": max(coordinate_multiplicities, default=0),
            "median_positions_per_root": median(coordinate_multiplicities) if coordinate_multiplicities else 0,
        },
        "graph_inventory": {
            "unique_directed_pairs": len(edges),
            "graph_nodes": len(graph_nodes),
            "nodes_with_coordinates": len(covered_nodes),
            "node_coordinate_coverage": len(covered_nodes) / len(graph_nodes) if graph_nodes else 0.0,
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
        "null_design_status": {
            "distance_only": "candidate sensitivity control",
            "degree_plus_distance": "primary Gate C candidate",
            "npc_plus_distance": "secondary candidate if computationally feasible",
            "edr": "projectome/neuropil sensitivity control; not a neuron-level NPC replacement",
        },
        "missing_coordinate_policy": "pairs with missing endpoint coordinates are excluded from distance summaries and counted through coverage metrics",
        "duplicate_coordinate_policy": "collapse all rows for each root_id using component-wise median; report multiplicity instead of silently keeping the first row",
        "scientific_conclusion": None,
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
