#!/usr/bin/env python3
"""Run the deterministic M6 RSS benchmark and emit CSV."""
from __future__ import annotations
import csv
from pathlib import Path
from src.simulator.rss_benchmark import RSSSweepConfig, default_rss_cases, run_rss_case

def main() -> None:
    out = Path("artifacts/m6-rss/results.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    config = RSSSweepConfig(modules=12, state_dim=4, contexts=3, sequence_length=12,
                            max_active_relations=8, max_higher_order=2, bytes_per_relation=8)
    rows = []
    for case in default_rss_cases(config):
        rows.extend(run_rss_case(case, config))
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["case","task","context","target","prediction","error",
                         "active_relations","transmitted_bytes","routing_churn","higher_order_relations"])
        for r in rows:
            writer.writerow([r.case,r.task,r.context,r.target,r.prediction,r.error,
                             r.active_relations,r.transmitted_bytes,r.routing_churn,r.higher_order_relations])
    print(f"wrote {len(rows)} rows to {out}")

if __name__ == "__main__":
    main()
