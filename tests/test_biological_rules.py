from pathlib import Path
from src.graph.biological_rules import BiologicalRule, load_rules, save_rules

def test_rule_round_trip(tmp_path: Path):
    rules = [BiologicalRule("BR-001", "Example", "test", "degree-preserving", "z=3", "example", "event-driven routing", "latency and energy")]
    path = tmp_path / "rules.json"
    save_rules(rules, path)
    assert load_rules(path) == rules
