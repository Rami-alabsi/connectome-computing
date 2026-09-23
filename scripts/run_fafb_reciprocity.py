#!/usr/bin/env python3
"""Compute reciprocity and reciprocal-degree statistics for FAFB v783."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
from collections import Counter
from src.graph.connections import _open_csv,_pick,SOURCE_CANDIDATES,TARGET_CANDIDATES

def load_edges(path):
    edges=set()
    with _open_csv(path) as fh:
        reader=csv.DictReader(fh)
        s=_pick(reader.fieldnames,SOURCE_CANDIDATES); t=_pick(reader.fieldnames,TARGET_CANDIDATES)
        for row in reader:
            u,v=row[s],row[t]
            if u!=v: edges.add((u,v))
    return edges

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/reciprocity.json")
    args=ap.parse_args()
    edges=load_edges(Path(args.input))
    reciprocal_pairs=sum(1 for u,v in edges if (v,u) in edges)
    reciprocal_connections=reciprocal_pairs
    reciprocal_degree=Counter()
    for u,v in edges:
        if (v,u) in edges:
            reciprocal_degree[u]+=1
    nodes={x for e in edges for x in e}
    vals=list(reciprocal_degree.values())
    result={
      "dataset":"FAFB","version":"v783",
      "unique_directed_pairs":len(edges),
      "reciprocity_probability": reciprocal_pairs/len(edges) if edges else 0.0,
      "reciprocal_directed_edge_count":reciprocal_connections,
      "nodes_with_reciprocal_edges":sum(1 for n in nodes if reciprocal_degree[n]>0),
      "reciprocal_degree_mean_over_nodes":sum(vals)/len(nodes) if nodes else 0.0,
      "reciprocal_degree_max":max(vals,default=0),
      "definition":"P[v->u | u->v], computed on unique directed non-self pairs."
    }
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
