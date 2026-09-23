#!/usr/bin/env python3
"""Download a pinned public FlyWire/Codex FAFB resource.

Codex documents the static-download API as the supported programmatic path.
The FAFB dataset selector currently resolves to v783. The script defaults to
the consolidated connection table used by the project's streaming parser and
writes the compressed resource without loading it into memory.
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://codex.flywire.ai/api/download_resource"

def download(dataset: str, data_product: str, output: Path) -> None:
    token = os.environ.get("CODEX_API_TOKEN")
    if not token:
        raise RuntimeError("CODEX_API_TOKEN is required for Codex static downloads; set it from your Codex account.")
    query = urllib.parse.urlencode({"data_product": data_product, "dataset": dataset, "api_token": token})
    url = f"{BASE}?{query}"
    output.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "connectome-computing/0.1"},
    )
    with urllib.request.urlopen(request, timeout=120) as response, output.open("wb") as dst:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            dst.write(chunk)

    metadata = {
        "dataset": dataset,
        "data_product": data_product,
        "source_url": url,
        "output": str(output),
        "note": "Codex static download; verify dataset/version metadata before scientific analysis.",
    }
    output.with_suffix(output.suffix + ".json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"downloaded {output} ({output.stat().st_size} bytes)")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="fafb")
    parser.add_argument("--data-product", default="connections_princeton")
    parser.add_argument(
        "--output",
        default="data/raw/fafb_v783/connections_princeton.csv.gz",
    )
    args = parser.parse_args()
    download(args.dataset, args.data_product, Path(args.output))

if __name__ == "__main__":
    main()
