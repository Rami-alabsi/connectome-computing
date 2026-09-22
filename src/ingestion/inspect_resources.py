"""Print the current Codex resources for a dataset."""

from __future__ import annotations
import argparse
import json
from codex import list_resources

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="fafb")
    args = parser.parse_args()
    print(json.dumps(list_resources(args.dataset), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
