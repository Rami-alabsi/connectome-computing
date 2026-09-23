from pathlib import Path

from scripts.analyze_m6_rss import summarize


def test_summary_uses_seed_means_as_replicates(tmp_path: Path):
    path = tmp_path / "results.csv"
    path.write_text(
        "seed,budget,case,task,error\n"
        "0,4,C,context,1.0\n"
        "0,4,C,context,3.0\n"
        "1,4,C,context,2.0\n"
        "1,4,C,context,4.0\n",
        encoding="utf-8",
    )
    rows = summarize(path)
    assert len(rows) == 1
    row = rows[0]
    assert row["n_seeds"] == 2
    assert row["mean_seed_error"] == 2.5
    assert row["std_seed_error"] > 0.0
    assert row["ci95_low"] < 2.5 < row["ci95_high"]
