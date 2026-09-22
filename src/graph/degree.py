"""Degree-distribution and hub statistics for directed connectomes."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from math import sqrt
from typing import Iterable

@dataclass(frozen=True)
class DegreeProfile:
    nodes: int
    directed_edges: int
    mean_in: float
    mean_out: float
    median_in: float
    median_out: float
    p90_in: float
    p90_out: float
    p99_in: float
    p99_out: float
    max_in: int
    max_out: int
    in_cv: float
    out_cv: float
    hub_fraction_in: float
    hub_fraction_out: float
    in_out_pearson: float

def _percentile(values: list[int], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    if len(values) == 1:
        return float(values[0])
    position = (len(values) - 1) * q
    lo = int(position)
    hi = min(lo + 1, len(values) - 1)
    frac = position - lo
    return values[lo] * (1 - frac) + values[hi] * frac

def _cv(values: list[int]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return sqrt(variance) / mean

def _pearson(a: list[int], b: list[int]) -> float:
    if len(a) != len(b) or not a:
        return 0.0
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    da = [x - ma for x in a]
    db = [y - mb for y in b]
    denom = sqrt(sum(x * x for x in da) * sum(y * y for y in db))
    return sum(x * y for x, y in zip(da, db)) / denom if denom else 0.0

def degree_profile(
    edges: Iterable[tuple[str, str]],
    *,
    nodes: Iterable[str] | None = None,
    hub_multiplier: float = 5.0,
) -> DegreeProfile:
    """Measure directed degree distributions and a transparent hub threshold."""
    clean = {(u, v) for u, v in edges if u != v}
    node_set = set(nodes or ())
    node_set.update(u for u, _ in clean)
    node_set.update(v for _, v in clean)
    ordered = sorted(node_set)
    indeg = {n: 0 for n in ordered}
    outdeg = {n: 0 for n in ordered}
    for u, v in clean:
        outdeg[u] += 1
        indeg[v] += 1
    ins = [indeg[n] for n in ordered]
    outs = [outdeg[n] for n in ordered]
    mean_in = sum(ins) / len(ins) if ins else 0.0
    mean_out = sum(outs) / len(outs) if outs else 0.0
    hub_in = sum(x >= hub_multiplier * mean_in for x in ins) / len(ins) if ins else 0.0
    hub_out = sum(x >= hub_multiplier * mean_out for x in outs) / len(outs) if outs else 0.0
    return DegreeProfile(
        len(ordered), len(clean), mean_in, mean_out,
        _percentile(ins, .5), _percentile(outs, .5),
        _percentile(ins, .9), _percentile(outs, .9),
        _percentile(ins, .99), _percentile(outs, .99),
        max(ins, default=0), max(outs, default=0),
        _cv(ins), _cv(outs), hub_in, hub_out, _pearson(ins, outs)
    )

def to_dict(profile: DegreeProfile) -> dict[str, float | int]:
    return asdict(profile)
