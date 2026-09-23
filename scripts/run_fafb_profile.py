#!/usr/bin/env python3
"""Build a reproducible first-pass FAFB v783 structural profile."""
from __future__ import annotations
import argparse, csv, gzip, json
from pathlib import Path
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES, WEIGHT_CANDIDATES
from src.graph.stats import degree_statistics
from src.graph.degree import degree_profile, to_dict as degree_to_dict

def unique_edges(path: Path):
    seen=set()
    with _open_csv(path) as fh:
        reader=csv.DictReader(fh)
        source=_pick(reader.fieldnames, SOURCE_CANDIDATES)
        target=_pick(reader.fieldnames, TARGET_CANDIDATES)
        for row in reader:
            pair=(row[source],row[target])
            if pair not in seen:
                seen.add(pair)
                yield pair

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/profile.json")
    args=ap.parse_args()
    path=Path(args.input)
    edges=list(unique_edges(path))
    nodes=set()
    for u,v in edges: nodes.update((u,v))
    result={
        "dataset":"FAFB",
        "materialization":"v783",
        "connection_table":str(path),
        "connection_summary": {
            "nodes_in_connection_table": len(nodes),
            "unique_directed_pairs": len(edges),
        },
        "degree_statistics": degree_statistics(path),
        "degree_profile": degree_to_dict(degree_profile(edges,nodes=nodes)),
        "method_note":"Degree metrics use unique directed neuron pairs, not raw region-split connection rows.",
    }
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__": main()
