#!/usr/bin/env python3
"""Aggregate independently generated FAFB CFG null artifacts."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--expected-nulls", type=int, default=100)
    args = ap.parse_args()

    files = sorted(Path(args.input_dir).glob("null-*.json"))
    if len(files) != args.expected_nulls:
        raise RuntimeError(
            f"expected {args.expected_nulls} null artifacts, found {len(files)}"
        )

    artifacts = [json.loads(p.read_text(encoding="utf-8")) for p in files]
    first = artifacts[0]

    for artifact in artifacts:
        if artifact["dataset"] != "FAFB" or artifact["version"] != "v783":
            raise RuntimeError("dataset/version mismatch")
        if artifact["unique_directed_pairs"] != first["unique_directed_pairs"]:
            raise RuntimeError("unique directed pair count mismatch")
        if artifact["thresholds"] != first["thresholds"]:
            raise RuntimeError("threshold grid mismatch")
        if artifact["min_synapses_per_connection"] != 5:
            raise RuntimeError("all nulls must use the 5-synapse threshold")
        if artifact["nulls"] != 1:
            raise RuntimeError("each input artifact must contain exactly one null")
        if not all(artifact["degree_preservation"]):
            raise RuntimeError("degree-preservation invariant failed")
        stats = artifact["swap_stats"][0]
        if not stats["fully_reached_target"]:
            raise RuntimeError("a null did not reach the requested swap target")

    observed = first["curve"]
    for artifact in artifacts[1:]:
        for a, b in zip(observed, artifact["curve"]):
            if a["rich_nodes"] != b["rich_nodes"] or a["rich_edges"] != b["rich_edges"]:
                raise RuntimeError("observed curve differs across null artifacts")

    rows = []
    for i, obs in enumerate(observed):
        values = [a["curve"][i]["null_mean_density"] for a in artifacts]
        mean = sum(values) / len(values)
        sd = math.sqrt(sum((x - mean) ** 2 for x in values) / (len(values) - 1))
        ratio = obs["rich_density"] / mean if mean else None
        rows.append({
            **obs,
            "null_mean_density": mean,
            "null_sd_density": sd,
            "observed_to_null": ratio,
            "phi_norm": ratio,
            "above_1pct": bool(ratio is not None and ratio > 1.01),
            "null_count": len(values),
        })

    above = [r["threshold"] for r in rows if r["above_1pct"]]
    peak = max(rows, key=lambda r: r["phi_norm"] if r["phi_norm"] is not None else float("-inf"))

    result = {
        "dataset": "FAFB",
        "version": "v783",
        "unique_directed_pairs": first["unique_directed_pairs"],
        "degree_definition": first["degree_definition"],
        "min_synapses_per_connection": 5,
        "null_model": first["null_model"],
        "nulls": len(artifacts),
        "successful_swaps_target": first["successful_swaps_target"],
        "swap_stats": [a["swap_stats"][0] for a in artifacts],
        "thresholds": first["thresholds"],
        "degree_preservation": [a["degree_preservation"][0] for a in artifacts],
        "curve": rows,
        "rich_club_criterion": "phi_norm > 1.01",
        "onset_threshold": min(above) if above else None,
        "offset_threshold": max(above) if above else None,
        "peak_threshold": peak["threshold"],
        "peak_phi_norm": peak["phi_norm"],
        "source_null_artifacts": [p.name for p in files],
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "nulls": len(artifacts),
        "peak_threshold": peak["threshold"],
        "peak_phi_norm": peak["phi_norm"],
        "onset_threshold": result["onset_threshold"],
        "offset_threshold": result["offset_threshold"],
    }, indent=2))


if __name__ == "__main__":
    main()
