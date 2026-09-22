"""Streaming utilities for Codex connection tables.
Codex connection exports can contain multiple rows for the same neuron pair when
synapses occur in different regions. This module preserves those rows.
"""
from __future__ import annotations
import csv, gzip
from collections import Counter
from pathlib import Path
from typing import Iterable, Iterator, Mapping, TextIO

SOURCE_CANDIDATES = ("pre_root_id", "pre_root", "presynaptic_root_id", "source_root_id")
TARGET_CANDIDATES = ("post_root_id", "post_root", "postsynaptic_root_id", "target_root_id")
WEIGHT_CANDIDATES = ("syn_count", "synapse_count", "n_synapses", "weight")

def _open_csv(path: str | Path) -> TextIO:
    p = Path(path)
    return gzip.open(p, "rt", encoding="utf-8", newline="") if p.suffix == ".gz" else p.open("r", encoding="utf-8", newline="")

def _pick(fieldnames: Iterable[str], candidates: Iterable[str]) -> str:
    fields = set(fieldnames)
    for name in candidates:
        if name in fields:
            return name
    raise ValueError(f"None of {tuple(candidates)} found in columns: {sorted(fields)}")

def iter_connections(path: str | Path) -> Iterator[Mapping[str, str]]:
    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Connection file has no CSV header")
        yield from reader

def summarize(path: str | Path) -> dict:
    nodes: set[str] = set()
    pair_counts: Counter[tuple[str, str]] = Counter()
    edge_rows = 0
    total_synapses = 0
    weight_column = None

    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Connection file has no CSV header")
        source = _pick(reader.fieldnames, SOURCE_CANDIDATES)
        target = _pick(reader.fieldnames, TARGET_CANDIDATES)
        for row in reader:
            s, t = row[source], row[target]
            nodes.update((s, t))
            edge_rows += 1
            pair_counts[(s, t)] += 1
            if weight_column is None:
                weight_column = next((c for c in WEIGHT_CANDIDATES if c in row), None)
            if weight_column:
                try:
                    total_synapses += int(float(row[weight_column]))
                except (TypeError, ValueError):
                    pass

    return {
        "nodes": len(nodes),
        "edge_rows": edge_rows,
        "unique_directed_pairs": len(pair_counts),
        "multi_region_pair_rows": sum(v - 1 for v in pair_counts.values() if v > 1),
        "total_synapses": total_synapses if weight_column else None,
        "source_column": source,
        "target_column": target,
        "weight_column": weight_column,
    }
