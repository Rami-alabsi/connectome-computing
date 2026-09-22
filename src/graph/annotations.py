"""Utilities for joining Codex neuron annotations to graph analyses."""
from __future__ import annotations
import csv, gzip
from collections import Counter
from pathlib import Path
from typing import Iterator

def _open_csv(path: str | Path):
    p = Path(path)
    return gzip.open(p, "rt", encoding="utf-8", newline="") if p.suffix == ".gz" else p.open("r", encoding="utf-8", newline="")

def iter_annotations(path: str | Path) -> Iterator[dict[str, str]]:
    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Annotation file has no CSV header")
        yield from reader

def _first_column(fieldnames: list[str], candidates: tuple[str, ...]) -> str:
    for candidate in candidates:
        if candidate in fieldnames:
            return candidate
    raise ValueError(f"None of {candidates} found in columns: {fieldnames}")

def summarize_annotations(path: str | Path) -> dict:
    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Annotation file has no CSV header")
        fields = list(reader.fieldnames)
        root_column = _first_column(fields, ("root_id", "root", "root_id_x", "pt_root_id"))
        candidate_columns = {
            "cell_type": ("cell_type", "celltype", "type", "super_class"),
            "neuropil": ("neuropil", "primary_neuropil", "region"),
            "neurotransmitter": ("nt_type", "neurotransmitter", "nt"),
        }
        selected = {label: next((c for c in candidates if c in fields), None) for label, candidates in candidate_columns.items()}
        counts = {label: Counter() for label in selected}
        rows, roots = 0, set()
        for row in reader:
            rows += 1
            roots.add(row[root_column])
            for label, column in selected.items():
                if column:
                    value = row.get(column, "").strip()
                    if value:
                        counts[label][value] += 1
    return {
        "rows": rows,
        "unique_neurons": len(roots),
        "root_column": root_column,
        "selected_columns": selected,
        "top_values": {label: counts[label].most_common(20) for label in counts},
    }

def build_annotation_index(path: str | Path, *, root_column: str | None = None, fields: tuple[str, ...] = ("cell_type", "neuropil", "neurotransmitter")) -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    with _open_csv(path) as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Annotation file has no CSV header")
        columns = list(reader.fieldnames)
        root = root_column or _first_column(columns, ("root_id", "root", "root_id_x", "pt_root_id"))
        for row in reader:
            rid = row[root]
            index[rid] = {field: row.get(field, "").strip() for field in fields if field in row and row.get(field, "").strip()}
    return index
