#!/usr/bin/env python3
"""Estimate FAFB v783 rich-club enrichment against degree-preserving nulls."""
from __future__ import annotations
import argparse, csv, json, math, random
from pathlib import Path
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES
from src.graph.random_baseline import degree_preserving_randomization, degree_preservation_report

def load_edges(path, min_synapses=0):
    """Load unique directed pairs after aggregating synapses across region rows."""
    pair_synapses={}
    with _open_csv(path) as fh:
        reader=csv.DictReader(fh)
        s=_pick(reader.fieldnames,SOURCE_CANDIDATES)
        t=_pick(reader.fieldnames,TARGET_CANDIDATES)
        w=_pick(reader.fieldnames, ("syn_count","synapse_count","n_synapses","weight"))
        for row in reader:
            u,v=row[s],row[t]
            if u==v:
                continue
            try:
                weight=float(row[w])
            except (TypeError, ValueError):
                weight=0.0
            pair_synapses[(u,v)] = pair_synapses.get((u,v), 0.0) + weight
    return {pair for pair,total in pair_synapses.items() if total >= min_synapses}

def curve(edges, thresholds):
    indeg={}
    outdeg={}
    for u,v in edges:
        outdeg[u]=outdeg.get(u,0)+1
        indeg[v]=indeg.get(v,0)+1
    totaldeg={u:indeg.get(u,0)+outdeg.get(u,0) for u in set(indeg)|set(outdeg)}
    out=[]
    n=len(edges)
    for k in thresholds:
        rich={u for u,d in totaldeg.items() if d>=k}
        possible=len(rich)*(len(rich)-1)
        re=sum(1 for u,v in edges if u in rich and v in rich)
        density=re/possible if possible else 0.0
        cross=sum(1 for u,v in edges if (u in rich) ^ (v in rich))
        out.append({"threshold":k,"rich_nodes":len(rich),"rich_edges":re,
                    "rich_density":density,"cross_fraction":cross/n if n else 0.0})
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/rich-club.json")
    ap.add_argument("--nulls",type=int,default=2)
    ap.add_argument("--seed-offset",type=int,default=0,
                    help="offset applied to null seeds; preserves independent per-null RNG streams")
    ap.add_argument("--swaps-per-edge",type=float,default=1.0)
    ap.add_argument("--min-synapses",type=float,default=0,
                    help="minimum synapses per neuron pair; 0 keeps all unique pairs")
    ap.add_argument("--thresholds",default="",help="comma-separated total-degree thresholds; overrides quantile thresholds")
    ap.add_argument("--threshold-min",type=int,default=None)
    ap.add_argument("--threshold-max",type=int,default=None)
    ap.add_argument("--threshold-step",type=int,default=1)
    args=ap.parse_args()
    edges=load_edges(Path(args.input), args.min_synapses)
    indeg={}
    outdeg={}
    for u,v in edges:
        outdeg[u]=outdeg.get(u,0)+1
        indeg[v]=indeg.get(v,0)+1
    totaldeg={u:indeg.get(u,0)+outdeg.get(u,0) for u in set(indeg)|set(outdeg)}
    vals=sorted(totaldeg.values())
    if args.thresholds:
        thresholds=sorted({int(x.strip()) for x in args.thresholds.split(",") if x.strip()})
    elif args.threshold_min is not None and args.threshold_max is not None:
        if args.threshold_step <= 0 or args.threshold_min > args.threshold_max:
            raise ValueError("invalid threshold range")
        thresholds=list(range(args.threshold_min,args.threshold_max+1,args.threshold_step))
    else:
        thresholds=sorted(set(max(1,int(vals[int((len(vals)-1)*q)])) for q in (0.90,0.95,0.99,0.995)))
    if not thresholds:
        raise ValueError("at least one threshold is required")
    observed=curve(edges,thresholds)
    null_curves=[]
    preservation=[]
    swap_stats=[]
    swaps=max(1000,int(len(edges)*args.swaps_per_edge))
    for local_seed in range(args.nulls):
        seed = args.seed_offset + local_seed
        null, stats=degree_preserving_randomization(edges,swaps=swaps,seed=seed,return_stats=True)
        preservation.append(degree_preservation_report(edges,null))
        swap_stats.append({"seed":seed,**stats})
        null_curves.append(curve(null,thresholds))
    rows=[]
    for i,o in enumerate(observed):
        nd=[c[i]["rich_density"] for c in null_curves]
        mean=sum(nd)/len(nd) if nd else 0.0
        sd=(sum((x-mean)**2 for x in nd)/(len(nd)-1))**0.5 if len(nd)>1 else None
        ratio=o["rich_density"]/mean if mean else None
        rows.append({**o,"null_mean_density":mean,"null_sd_density":sd,
                     "observed_to_null":ratio,
                     "phi_norm":ratio,
                     "above_1pct":bool(ratio is not None and ratio > 1.01)})
    above=[r["threshold"] for r in rows if r["above_1pct"]]
    result={"dataset":"FAFB","version":"v783","unique_directed_pairs":len(edges),
            "degree_definition":"total degree = in-degree + out-degree on unique directed pairs",
            "min_synapses_per_connection":args.min_synapses,
            "null_model":"directed degree-preserving edge swaps",
            "nulls":args.nulls,"successful_swaps_target":swaps,"swap_stats":swap_stats,
            "thresholds":thresholds,"degree_preservation":preservation,"curve":rows,
            "rich_club_criterion":"phi_norm > 1.01",
            "onset_threshold":min(above) if above else None,
            "offset_threshold":max(above) if above else None,
            "peak_threshold":max(rows,key=lambda r: r["phi_norm"] if r["phi_norm"] is not None else float("-inf"))["threshold"] if rows else None}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
