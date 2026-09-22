"""Analyze a downloaded Codex connection CSV."""
from __future__ import annotations
import argparse, json
from src.graph.connections import summarize
from src.graph.stats import degree_statistics

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    print(json.dumps({'summary': summarize(args.path), 'degree_statistics': degree_statistics(args.path)}, indent=2))

if __name__ == '__main__':
    main()