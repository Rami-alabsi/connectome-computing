#!/usr/bin/env python3
"""Summarize M6 RSS results with seed-level uncertainty.

The unit of replication is the seed, not an individual timestep. For each
(case, budget, task), this script first averages error within each seed and
then reports the mean, sample standard deviation and a normal-approximation
95% confidence interval across seeds.

No ranking or composite score is produced.
"""
from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

Z95 = 1.959963984540054

def summarize(path: Path) -> list[dict[str, object]]:
    groups: dict[tuple[str, int, str, int], list[float]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["case"], int(row["budget"]), row["task"], int(row["seed"]))
            groups[key].append(float(row["error"]))

    seed_means: dict[tuple[str, int, str], list[float]] = defaultdict(list)
    for (case, budget, task, _seed), values in groups.items():
        if not values:
            continue
        seed_means[(case, budget, task)].append(sum(values) / len(values))

    rows: list[dict[str, object]] = []
    for (case, budget, task), values in sorted(seed_means.items()):
        n = len(values)
        mean = sum(values) / n
        if n > 1:
            variance = sum((x - mean) ** 2 for x in values) / (n - 1)
            std = math.sqrt(variance)
            half_width = Z95 * std / math.sqrt(n)
        else:
            std = 0.0
            half_width = float("nan")
        rows.append({
            "case": case,
            "budget": budget,
            "task": task,
            "n_seeds": n,
            "mean_seed_error": mean,
            "std_seed_error": std,
            "ci95_low": mean - half_width if n > 1 else float("nan"),
            "ci95_high": mean + half_width if n > 1 else float("nan"),
        })
    return rows

def write_summary(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "case", "budget", "task", "n_seeds",
        "mean_seed_error", "std_seed_error", "ci95_low", "ci95_high",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def main() -> None:
    input_path = Path("artifacts/m6-rss/results.csv")
    output_path = Path("artifacts/m6-rss/summary.csv")
    rows = summarize(input_path)
    write_summary(rows, output_path)
    print(f"wrote {len(rows)} summary rows to {output_path}")

if __name__ == "__main__":
    main()
