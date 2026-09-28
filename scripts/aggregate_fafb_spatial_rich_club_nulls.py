#!/usr/bin/env python3
"""Aggregate validated FAFB v783 hard-binned arbor-spatial nulls."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    docs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in args.inputs]
    if not docs:
        raise ValueError("no nulls")
    expected = docs[0]
    keys = ("unique_directed_pairs", "full_nodes", "min_synapses_per_connection", "thresholds", "distance_bins_nm")
    for d in docs[1:]:
        for k in keys:
            if d[k] != expected[k]:
                raise ValueError(f"mismatch in {k}")
    if any(not all(d["preservation"].values()) for d in docs):
        raise ValueError("one or more nulls failed preservation invariants")
    observed = expected["observed_curve"]
    for d in docs[1:]:
        if d["observed_curve"] != observed:
            raise ValueError("observed curve mismatch")
    rows = []
    for i, obs in enumerate(observed):
        vals = [d["null_curve"][i]["rich_density"] for d in docs]
        mean = sum(vals) / len(vals)
        sd = (sum((x - mean) ** 2 for x in vals) / (len(vals) - 1)) ** 0.5 if len(vals) > 1 else None
        ratio = obs["rich_density"] / mean if mean else None
        rows.append({
            **obs,
            "null_mean_density": mean,
            "null_sd_density": sd,
            "observed_to_null": ratio,
            "phi_norm": ratio,
            "above_1pct": bool(ratio is not None and ratio > 1.01),
        })
    above = [r["threshold"] for r in rows if r["above_1pct"]]
    result = {
        "dataset": "FAFB",
        "version": "v783",
        "purpose": "Gate C spatial hard-binned arbor-distance rich-club null ensemble",
        "null_model": expected["null_model"],
        "nulls": len(docs),
        "seeds": [d["seed"] for d in docs],
        "unique_directed_pairs": expected["unique_directed_pairs"],
        "full_nodes": expected["full_nodes"],
        "min_synapses_per_connection": expected["min_synapses_per_connection"],
        "thresholds": expected["thresholds"],
        "distance_bins_nm": expected["distance_bins_nm"],
        "all_invariants_preserved": True,
        "swap_stats": [dict(seed=d["seed"], **d["swap_stats"]) for d in docs],
        "curve": rows,
        "rich_club_criterion": "phi_norm > 1.01 (descriptive only)",
        "onset_threshold": min(above) if above else None,
        "offset_threshold": max(above) if above else None,
        "peak_threshold": max(rows, key=lambda r: r["phi_norm"] if r["phi_norm"] is not None else float("-inf"))["threshold"] if rows else None,
        "scientific_conclusion": None,
        "interpretation_rule": "This ensemble is a project-defined spatial sensitivity control; compare with CFG and NPC-like results without treating it as a mechanistic or exact literature reproduction.",
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "nulls": len(docs),
        "all_invariants_preserved": True,
        "onset_threshold": result["onset_threshold"],
        "offset_threshold": result["offset_threshold"],
        "peak_threshold": result["peak_threshold"],
    }, indent=2))

if __name__ == "__main__":
    main()
