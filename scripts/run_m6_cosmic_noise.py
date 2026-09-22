#!/usr/bin/env python3
"""Run the deterministic M6 noise-robustness sweep."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from src.simulator.noise_benchmark import NoiseCase, run_noise_case


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", nargs="+", type=int, default=[100, 1000, 10000])
    parser.add_argument("--state-dim", type=int, default=8)
    parser.add_argument("--field-dims", nargs="+", type=int, default=[2, 4, 8])
    parser.add_argument("--active-pairs", nargs="+", type=int, default=[1, 4, 16])
    parser.add_argument("--noise", nargs="+", type=float, default=[0.0, 0.01, 0.05, 0.1])
    parser.add_argument("--seeds", nargs="+", type=int, default=[0, 1, 2])
    parser.add_argument("--output", default="results/m6-cosmic-noise.csv")
    args = parser.parse_args()

    rows = []
    for nodes in args.nodes:
        for field_dim in args.field_dims:
            if field_dim > args.state_dim:
                continue
            for active_pairs in args.active_pairs:
                for noise_std in args.noise:
                    for seed in args.seeds:
                        for mode in ("full", "sparse", "field", "hybrid"):
                            result = run_noise_case(
                                nodes=nodes,
                                state_dim=args.state_dim,
                                case=NoiseCase(
                                    mode=mode,
                                    field_dim=field_dim,
                                    active_pairs=active_pairs,
                                    noise_std=noise_std,
                                    seed=seed,
                                ),
                            )
                            rows.append(result.__dict__)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
