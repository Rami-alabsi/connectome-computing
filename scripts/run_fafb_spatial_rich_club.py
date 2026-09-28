#!/usr/bin/env python3
# Bootstrap trigger: validated C1 -> four-null ensemble handoff.\n"""Run one FAFB v783 hard-binned arbor-spatial rich-club null.

This is a project-defined sensitivity null: directed degree-preserving swaps
must preserve the multiset of coarse arbor-distance bins. It is not an exact
reproduction of Lin et al.'s NND model and does not itself establish mechanism.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import random
from collections import Counter
from pathlib import Path

from src.graph.connections import aggregate_pair_synapses

BINS_NM = (
    0, 25_000, 50_000, 100_000, 200_000, 500_000,
    1_000_000, 2_000_000, 5_000_000, 10_000_000, float("inf")
)

def load_centroids(path):
    out, inc = {}, {}
    with gzip.open(path, "rt", newline="") as f:
        for row in csv.DictReader(f):
            rid = row["root_id"]
            out[rid] = (float(row["out_x"]), float(row["out_y"]), float(row["out_z"]))
            inc[rid] = (float(row["in_x"]), float(row["in_y"]), float(row["in_z"]))
    return out, inc

def distance_nm(a, b):
    dx = (a[0] - b[0]) * 4.0
    dy = (a[1] - b[1]) * 4.0
    dz = (a[2] - b[2]) * 40.0
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def dbin(x):
    for i in range(len(BINS_NM) - 1):
        if BINS_NM[i] <= x < BINS_NM[i + 1]:
            return i
    raise ValueError(x)

def degree_maps(edges):
    indeg, outdeg = Counter(), Counter()
    for u, v in edges:
        outdeg[u] += 1
        indeg[v] += 1
    return indeg, outdeg

def rich_curve(edges, thresholds):
    indeg, outdeg = degree_maps(edges)
    nodes = set(indeg) | set(outdeg)
    totaldeg = {n: indeg.get(n, 0) + outdeg.get(n, 0) for n in nodes}
    n = len(edges)
    rows = []
    for k in thresholds:
        rich = {u for u, d in totaldeg.items() if d >= k}
        possible = len(rich) * (len(rich) - 1)
        rich_edges = sum(1 for u, v in edges if u in rich and v in rich)
        cross = sum(1 for u, v in edges if (u in rich) ^ (v in rich))
        rows.append({
            "threshold": k,
            "rich_nodes": len(rich),
            "rich_edges": rich_edges,
            "rich_density": rich_edges / possible if possible else 0.0,
            "cross_fraction": cross / n if n else 0.0,
        })
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--connections", required=True)
    ap.add_argument("--centroids", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--swaps-per-edge", type=float, default=1.0)
    ap.add_argument("--min-synapses", type=int, default=5)
    ap.add_argument("--threshold-min", type=int, default=20)
    ap.add_argument("--threshold-max", type=int, default=120)
    ap.add_argument("--threshold-step", type=int, default=1)
    args = ap.parse_args()

    outc, inc = load_centroids(Path(args.centroids))
    edges = list(aggregate_pair_synapses(args.connections, min_synapses=args.min_synapses))
    full_nodes = {u for u, v in edges} | {v for u, v in edges}
    if not edges:
        raise ValueError("no edges")
    missing = [(u, v) for u, v in edges if u not in outc or v not in inc]
    if missing:
        raise ValueError(f"spatial coverage incomplete: {len(missing)} edges missing centroids")

    thresholds = list(range(args.threshold_min, args.threshold_max + 1, args.threshold_step))
    observed = rich_curve(edges, thresholds)

    edge_list = list(edges)
    edge_set = set(edge_list)
    edge_bins = [dbin(distance_nm(outc[u], inc[v])) for u, v in edge_list]
    initial_bins = Counter(edge_bins)
    initial_indeg, initial_outdeg = degree_maps(edge_list)

    rng = random.Random(args.seed)
    swaps = max(1000, int(len(edge_list) * args.swaps_per_edge))
    successful = attempts = invalid = bin_reject = 0
    max_attempts = max(100, swaps * 20)

    while successful < swaps and attempts < max_attempts:
        attempts += 1
        i, j = rng.sample(range(len(edge_list)), 2)
        a, b = edge_list[i]
        c, d = edge_list[j]
        if a == d or c == b or a == c or b == d:
            invalid += 1
            continue
        p1, p2 = (a, d), (c, b)
        if p1 in edge_set or p2 in edge_set or p1 == p2:
            invalid += 1
            continue
        old_bins = sorted((edge_bins[i], edge_bins[j]))
        new_bins = sorted((
            dbin(distance_nm(outc[a], inc[d])),
            dbin(distance_nm(outc[c], inc[b])),
        ))
        if old_bins != new_bins:
            bin_reject += 1
            continue
        edge_set.remove((a, b))
        edge_set.remove((c, d))
        edge_set.add(p1)
        edge_set.add(p2)
        edge_list[i], edge_list[j] = p1, p2
        edge_bins[i], edge_bins[j] = new_bins
        successful += 1

    final_indeg, final_outdeg = degree_maps(edge_list)
    preservation = {
        "same_edge_count": len(edge_list) == len(edge_set) == len(edges),
        "same_in_degree": initial_indeg == final_indeg,
        "same_out_degree": initial_outdeg == final_outdeg,
        "same_distance_bin_histogram": initial_bins == Counter(edge_bins),
        "fully_reached_target": successful >= swaps,
    }
    if not all(preservation.values()):
        raise RuntimeError(f"invariant failure: {preservation}")

    null_curve = rich_curve(edge_list, thresholds)
    result = {
        "dataset": "FAFB",
        "version": "v783",
        "purpose": "Gate C spatial hard-binned arbor-distance rich-club null",
        "null_model": "directed degree-preserving swaps with exact preservation of the multiset of coarse arbor-distance bins",
        "distance_definition": "anisotropic Euclidean from outgoing source arbor proxy centroid to incoming target arbor proxy centroid",
        "distance_bins_nm": list(BINS_NM),
        "unique_directed_pairs": len(edges),
        "full_nodes": len(full_nodes),
        "min_synapses_per_connection": args.min_synapses,
        "seed": args.seed,
        "swaps_target": swaps,
        "swap_stats": {
            "attempts": attempts,
            "successful_swaps": successful,
            "invalid_or_duplicate": invalid,
            "distance_bin_rejected": bin_reject,
            "acceptance_rate": successful / attempts if attempts else 0.0,
            "max_attempts": max_attempts,
        },
        "preservation": preservation,
        "thresholds": thresholds,
        "observed_curve": observed,
        "null_curve": null_curve,
        "scientific_conclusion": None,
        "limitations": [
            "project-defined spatial sensitivity null, not exact Lin et al. NND reproduction",
            "coarse distance bins are preserved rather than exact edge distances",
            "structural enrichment alone does not establish mechanism or computational function",
        ],
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "seed": args.seed,
        "successful_swaps": successful,
        "target": swaps,
        "fully_reached_target": preservation["fully_reached_target"],
        "acceptance_rate": preservation["fully_reached_target"] and successful / attempts,
    }, indent=2))

if __name__ == "__main__":
    main()
