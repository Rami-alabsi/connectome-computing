"""Download the two primary FAFB v783 analysis resources.

The resources are intentionally kept outside Git because biological datasets can
be large and are governed by their own terms. The script records checksums and
source URLs for reproducibility.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from .codex import download_resource, resource_url, sha256

DEFAULT_PRODUCTS = ("connections_princeton", "consolidated_cell_types")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/raw/fafb_v783")
    parser.add_argument("--dataset", default="fafb")
    parser.add_argument("--products", nargs="+", default=DEFAULT_PRODUCTS)
    args = parser.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    manifest = {"dataset": args.dataset, "resources": []}

    for product in args.products:
        filename = f"{product}.csv.gz"
        path = out / filename
        download_resource(product, path, args.dataset)
        manifest["resources"].append({
            "data_product": product,
            "path": str(path),
            "url": resource_url(product, args.dataset),
            "sha256": sha256(path),
        })

    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
