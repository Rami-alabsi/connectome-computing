"""Compare observed and synthetic structural profiles.

The comparison is intentionally descriptive: it reports discrepancies but does not
decide whether a synthetic graph is biologically valid.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

from .profile import StructuralProfile


@dataclass(frozen=True)
class ProfileComparison:
    observed: StructuralProfile
    synthetic: StructuralProfile
    absolute_error: dict[str, float]
    relative_error: dict[str, float]

    def to_dict(self) -> dict:
        return asdict(self)


def compare_profiles(observed: StructuralProfile, synthetic: StructuralProfile) -> ProfileComparison:
    fields = ("nodes", "directed_edges", "density", "mean_in_degree", "mean_out_degree", "reciprocal_edge_fraction")
    absolute = {}
    relative = {}
    for field in fields:
        a = float(getattr(observed, field))
        b = float(getattr(synthetic, field))
        absolute[field] = abs(b - a)
        relative[field] = abs(b - a) / abs(a) if a != 0 else (0.0 if b == 0 else float("inf"))
    return ProfileComparison(observed, synthetic, absolute, relative)


def save_comparison(comparison: ProfileComparison, path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(comparison.to_dict(), indent=2, allow_nan=True), encoding="utf-8")
