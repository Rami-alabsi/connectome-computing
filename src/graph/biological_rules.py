"""Structured records for traceable biological design rules."""
from __future__ import annotations
from dataclasses import asdict, dataclass
import json
from pathlib import Path

@dataclass(frozen=True)
class BiologicalRule:
    rule_id: str
    observation: str
    evidence: str
    null_model: str
    effect_size: str
    biological_context: str
    computational_hypothesis: str
    benchmark_required: str

def save_rules(rules: list[BiologicalRule], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps([asdict(rule) for rule in rules], indent=2, ensure_ascii=False), encoding="utf-8")

def load_rules(path: str | Path) -> list[BiologicalRule]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [BiologicalRule(**item) for item in data]
