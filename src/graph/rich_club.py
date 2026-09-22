from dataclasses import asdict, dataclass
from typing import Iterable

@dataclass(frozen=True)
class RichClubProfile:
    nodes: int
    edges: int
    threshold: int
    rich_nodes: int
    rich_edge_count: int
    rich_density: float
    normalized_rich_density: float
    rich_to_periphery_fraction: float

def rich_club_profile(edges: Iterable[tuple[str, str]], *, nodes: Iterable[str] | None = None,
                      degree_threshold: int = 0, null_rich_density: float | None = None) -> RichClubProfile:
    clean = {(u, v) for u, v in edges if u != v}
    node_set = set(nodes or ())
    node_set.update(u for u, _ in clean)
    node_set.update(v for _, v in clean)
    degree = {n: 0 for n in node_set}
    for u, v in clean:
        degree[u] += 1
        degree[v] += 1
    rich = {n for n, d in degree.items() if d >= degree_threshold}
    possible = len(rich) * (len(rich) - 1)
    rich_edges = sum(1 for u, v in clean if u in rich and v in rich)
    density = rich_edges / possible if possible else 0.0
    null = null_rich_density if null_rich_density and null_rich_density > 0 else None
    normalized = density / null if null else 1.0
    cross = sum(1 for u, v in clean if (u in rich) ^ (v in rich))
    cross_fraction = cross / len(clean) if clean else 0.0
    return RichClubProfile(len(node_set), len(clean), degree_threshold, len(rich),
                           rich_edges, density, normalized, cross_fraction)

def to_dict(profile: RichClubProfile) -> dict[str, float | int]:
    return asdict(profile)
