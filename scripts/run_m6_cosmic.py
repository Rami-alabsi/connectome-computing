#!/usr/bin/env python3
"""Run the first deterministic M6-COSMIC scaling/bandwidth sweep."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from src.simulator.multiscale_benchmark import MultiscaleCase, run_multiscale_case


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", nargs="+", type=int, default=[100, 1000, 10000])
    parser.add_argument("--state-dim", type=int, default=8)
    parser.add_argument("--field-dims", nargs="+", type=int, default=[1, 2, 4, 8])
    parser.add_argument("--active-pairs", nargs="+", type=int, default=[1, 4, 16])
    parser.add_argument("--output", default="results/m6-cosmic-scaling.csv")
    args = parser.parse_args()

    rows = []
    for nodes in args.nodes:
        for field_dim in args.field_dims:
            for active_pairs in args.active_pairs:
                for mode in ("full", "sparse", "field", "hybrid"):
                    if field_dim > args.state_dim:
                        continue
                    result = run_multiscale_case(
                        nodes=nodes,
                        state_dim=args.state_dim,
                        case=MultiscaleCase(
                            mode=mode,
                            field_dim=field_dim,
                            active_pairs=active_pairs,
                        ),
                    )
                    rows.append(result.__dict__)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
