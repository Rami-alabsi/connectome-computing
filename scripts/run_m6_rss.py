#!/usr/bin/env python3
"""Run the M6 RSS benchmark across matched communication budgets and seeds."""
from __future__ import annotations
import csv
import sys
from pathlib import Path

# Allow direct execution from the repository checkout (including CI runners).
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.simulator.rss_benchmark import RSSSweepConfig, default_rss_cases, run_rss_case

def main() -> None:
    out = Path("artifacts/m6-rss/results.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for seed in (0, 1, 2, 3, 4):
        for budget in (2, 4, 6, 8):
            config = RSSSweepConfig(
                modules=12, state_dim=4, contexts=3, sequence_length=12,
                max_active_relations=budget, max_higher_order=2,
                bytes_per_relation=8,
            )
            for base_case in default_rss_cases(config):
                case = type(base_case)(
                    name=base_case.name, mode=base_case.mode,
                    field_dim=base_case.field_dim,
                    max_active_relations=budget,
                    max_higher_order=base_case.max_higher_order,
                    bytes_per_relation=base_case.bytes_per_relation,
                    seed=seed,
                )
                for result in run_rss_case(case, config):
                    rows.append((seed, budget, result))
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "seed", "budget", "case", "task", "context", "target", "prediction",
            "error", "active_relations", "transmitted_bytes",
            "routing_churn", "higher_order_relations",
        ])
        for seed, budget, r in rows:
            writer.writerow([
                seed, budget, r.case, r.task, r.context, r.target, r.prediction,
                r.error, r.active_relations, r.transmitted_bytes,
                r.routing_churn, r.higher_order_relations,
            ])
    print(f"wrote {len(rows)} rows to {out}")

if __name__ == "__main__":
    main()
