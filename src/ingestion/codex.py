"""Dependency-light client for the public Codex download API."""

from __future__ import annotations

import gzip
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path
from dataclasses import dataclass

BASE_URL = "https://codex.flywire.ai"

@dataclass(frozen=True)
class Resource:
    name: str
    data_product: str
    dataset: str
    url: str

def _get_json(url: str) -> object:
    request = urllib.request.Request(url, headers={"User-Agent": "connectome-computing/0.1"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))

def list_resources(dataset: str = "fafb") -> object:
    """Return the current Codex download-resource catalogue."""
    query = urllib.parse.urlencode({"dataset": dataset})
    return _get_json(f"{BASE_URL}/api/download?{query}")

def resource_url(data_product: str, dataset: str = "fafb") -> str:
    """Build a Codex static-resource URL."""
    query = urllib.parse.urlencode({"data_product": data_product, "dataset": dataset})
    return f"{BASE_URL}/api/download_resource?{query}"

def download_resource(data_product: str, destination: str | Path, dataset: str = "fafb") -> Path:
    """Download one public Codex resource to disk."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(resource_url(data_product, dataset), headers={"User-Agent": "connectome-computing/0.1"})
    with urllib.request.urlopen(request, timeout=300) as response:
        with destination.open("wb") as output:
            while chunk := response.read(1024 * 1024):
                output.write(chunk)
    return destination

def sha256(path: str | Path) -> str:
    """Return the SHA-256 checksum of a local file."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def open_text(path: str | Path):
    """Open UTF-8 text, transparently handling gzip files."""
    path = Path(path)
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8", newline="")
    return path.open("r", encoding="utf-8", newline="")
