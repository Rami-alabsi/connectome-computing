"""Build a compact structural profile from a Codex connection CSV.

The parser is streaming: it never loads the complete connection table into RAM.
It expects source/target root IDs and optionally a synapse-count column.
"""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
from src.generator.profile import profile_from_edges, save_profile

SOURCE_COLUMNS = ("pre_root_id", "pre_root", "presynaptic_root_id", "source_root_id")
TARGET_COLUMNS = ("post_root_id", "post_root", "postsynaptic_root_id", "target_root_id")
WEIGHT_COLUMNS = ("syn_count", "synapse_count", "n_synapses", "weight")

def pick(columns, candidates):
    for name in candidates:
        if name in columns:
            return name
    raise ValueError(f"none of {candidates} found; columns={columns}")

def build_profile(path: str | Path):
    edges: set[tuple[str, str]] = set()
    total_synapses = 0.0
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header")
        source_col = pick(reader.fieldnames, SOURCE_COLUMNS)
        target_col = pick(reader.fieldnames, TARGET_COLUMNS)
        weight_col = next((x for x in WEIGHT_COLUMNS if x in reader.fieldnames), None)
        for row in reader:
            source, target = row[source_col], row[target_col]
            if not source or not target or source == target:
                continue
            edges.add((source, target))
            if weight_col:
                try:
                    total_synapses += float(row[weight_col] or 0)
                except ValueError:
                    pass
    return profile_from_edges(edges, total_synapses=total_synapses or None)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--output", default="results/fafb_profile.json")
    args = parser.parse_args()
    profile = build_profile(args.csv_path)
    save_profile(profile, args.output)
    print(profile)

if __name__ == "__main__":
    main()
