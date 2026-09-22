"""Connectome-derived computational architecture primitives."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class ArchitecturePrimitive:
    primitive_id: str
    name: str
    biological_basis: str
    structural_pattern: str
    computational_mechanism: str
    expected_property: str
    falsification_test: str
    status: str = "hypothesis"


DEFAULT_PRIMITIVES = [
    ArchitecturePrimitive(
        "AP-001",
        "Sparse Event Routing",
        "Sparse long-range connectivity",
        "Low edge density with selective communication",
        "Event-driven message passing between active nodes",
        "Reduced communication and energy cost under sparse workloads",
        "Compare against dense message passing at matched accuracy",
    ),
    ArchitecturePrimitive(
        "AP-002",
        "Recurrent State Loop",
        "Recurrent biological connectivity",
        "Directed feedback cycles",
        "Persistent local state with recurrent updates",
        "Improved temporal-task performance per unit communication",
        "Ablate recurrent edges and compare temporal benchmarks",
    ),
    ArchitecturePrimitive(
        "AP-003",
        "Modular Processing Unit",
        "Community/modular organization",
        "Dense within-module and sparse between-module connectivity",
        "Partition computation into semi-independent modules",
        "Lower cross-module traffic for decomposable workloads",
        "Compare modular and degree-matched non-modular networks",
    ),
    ArchitecturePrimitive(
        "AP-004",
        "Hub-Mediated Integration",
        "Highly connected hub neurons",
        "Small set of high-degree integration nodes",
        "Selective aggregation and routing across modules",
        "Fewer communication steps for cross-module integration",
        "Remove hubs while preserving total edge count and benchmark performance",
    ),
    ArchitecturePrimitive(
        "AP-005",
        "Motif Microcircuit",
        "Statistically enriched directed motifs",
        "Repeated local connectivity patterns",
        "Reusable small recurrent/feed-forward computation",
        "Motif-preserving networks outperform motif-destroyed controls on the target task",
        "Randomize motif instances while preserving degree statistics",
    ),
]


def save_primitives(primitives: list[ArchitecturePrimitive], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps([asdict(item) for item in primitives], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def load_primitives(path: str | Path) -> list[ArchitecturePrimitive]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [ArchitecturePrimitive(**item) for item in data]
