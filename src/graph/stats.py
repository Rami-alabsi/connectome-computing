"""Structural graph statistics for connectome connection tables."""
from __future__ import annotations
import csv, gzip
from collections import Counter
from pathlib import Path

from .connections import SOURCE_CANDIDATES, TARGET_CANDIDATES, WEIGHT_CANDIDATES, _pick, _open_csv

def degree_statistics(path: str | Path) -> dict:
    indegree: Counter[str] = Counter()
    outdegree: Counter[str] = Counter()
    pairs: set[tuple[str, str]] = set()
    nodes: set[str] = set()
    weighted_edges = 0

    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Connection file has no CSV header")
        source = _pick(reader.fieldnames, SOURCE_CANDIDATES)
        target = _pick(reader.fieldnames, TARGET_CANDIDATES)
        weight = next((c for c in WEIGHT_CANDIDATES if c in reader.fieldnames), None)

        for row in reader:
            s, t = row[source], row[target]
            nodes.update((s, t))
            outdegree[s] += 1
            indegree[t] += 1
            pairs.add((s, t))
            if weight:
                try:
                    weighted_edges += int(float(row[weight]))
                except (TypeError, ValueError):
                    pass

    reciprocal_pairs = sum(1 for s, t in pairs if s != t and (t, s) in pairs)
    non_self_pairs = sum(1 for s, t in pairs if s != t)

    def summary(values: Counter[str]) -> dict:
        if not values:
            return {"min": 0, "max": 0, "mean": 0.0}
        vals = list(values.values())
        return {"min": min(vals), "max": max(vals), "mean": sum(vals) / len(vals)}

    return {
        "nodes": len(nodes),
        "unique_directed_pairs": len(pairs),
        "in_degree": summary(indegree),
        "out_degree": summary(outdegree),
        "reciprocal_pair_fraction": (reciprocal_pairs / non_self_pairs) if non_self_pairs else 0.0,
        "weighted_synapse_total": weighted_edges if weight else None,
    }
