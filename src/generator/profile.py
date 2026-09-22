"""Structural profiles used to parameterize synthetic connectome generation."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from math import sqrt
from pathlib import Path

@dataclass(frozen=True)
class StructuralProfile:
    nodes: int
    directed_edges: int
    density: float
    mean_in_degree: float
    mean_out_degree: float
    reciprocal_edge_fraction: float
    total_synapses: float | None = None
    median_in_degree: float = 0.0
    median_out_degree: float = 0.0
    p90_in_degree: float = 0.0
    p90_out_degree: float = 0.0
    p99_in_degree: float = 0.0
    p99_out_degree: float = 0.0
    max_in_degree: int = 0
    max_out_degree: int = 0
    in_degree_cv: float = 0.0
    out_degree_cv: float = 0.0

def _percentile(values: list[int], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    position = (len(values) - 1) * q
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    fraction = position - lower
    return values[lower] + (values[upper] - values[lower]) * fraction

def _cv(values: list[int]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return sqrt(variance) / mean

def profile_from_edges(edges: set[tuple[str, str]], nodes: int | None = None, total_synapses: float | None = None, node_ids: set[str] | None = None) -> StructuralProfile:
    """Build a profile while preserving explicitly declared isolates."""
    clean = {(u, v) for u, v in edges if u != v}
    node_set = set(node_ids or ())
    node_set.update(n for edge in clean for n in edge)
    node_count = nodes if nodes is not None else len(node_set)
    if node_count < len(node_set):
        raise ValueError("nodes cannot be smaller than the declared/observed node set")
    universe = set(node_set)
    universe.update(f"__isolate_{i}" for i in range(node_count - len(universe)))
    in_degree = {n: 0 for n in universe}
    out_degree = {n: 0 for n in universe}
    for source, target in clean:
        out_degree[source] += 1
        in_degree[target] += 1
    ins, outs = list(in_degree.values()), list(out_degree.values())
    density = len(clean) / (node_count * (node_count - 1)) if node_count > 1 else 0.0
    reciprocal = sum(1 for u, v in clean if (v, u) in clean)
    return StructuralProfile(
        node_count, len(clean), density,
        sum(ins) / node_count if node_count else 0.0,
        sum(outs) / node_count if node_count else 0.0,
        reciprocal / len(clean) if clean else 0.0, total_synapses,
        _percentile(ins, 0.5), _percentile(outs, 0.5),
        _percentile(ins, 0.9), _percentile(outs, 0.9),
        _percentile(ins, 0.99), _percentile(outs, 0.99),
        max(ins, default=0), max(outs, default=0), _cv(ins), _cv(outs)
    )

def save_profile(profile: StructuralProfile, path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(asdict(profile), indent=2), encoding="utf-8")

def load_profile(path: str | Path) -> StructuralProfile:
    return StructuralProfile(**json.loads(Path(path).read_text(encoding="utf-8")))
