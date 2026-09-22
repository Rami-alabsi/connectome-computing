"""Structural profiles used to parameterize synthetic connectome generation."""
from __future__ import annotations
from dataclasses import asdict, dataclass
import json
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

def profile_from_edges(
    edges: set[tuple[str, str]],
    nodes: int | None = None,
    total_synapses: float | None = None,
) -> StructuralProfile:
    clean = {(u, v) for u, v in edges if u != v}
    node_set = {n for edge in clean for n in edge}
    node_count = nodes if nodes is not None else len(node_set)
    density = len(clean) / (node_count * (node_count - 1)) if node_count > 1 else 0.0
    reciprocal = sum(1 for u, v in clean if (v, u) in clean)
    return StructuralProfile(
        node_count,
        len(clean),
        density,
        len(clean) / node_count if node_count else 0.0,
        len(clean) / node_count if node_count else 0.0,
        reciprocal / len(clean) if clean else 0.0,
        total_synapses,
    )

def save_profile(profile: StructuralProfile, path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(asdict(profile), indent=2), encoding="utf-8")

def load_profile(path: str | Path) -> StructuralProfile:
    return StructuralProfile(**json.loads(Path(path).read_text(encoding="utf-8")))
