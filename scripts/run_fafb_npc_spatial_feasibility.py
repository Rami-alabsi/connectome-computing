#!/usr/bin/env python3
"""C2 feasibility pilot: NPC-like block preservation + arbor-distance-bin preservation."""
from __future__ import annotations
import argparse, csv, gzip, json, math, random
from collections import Counter, defaultdict
from pathlib import Path
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES, aggregate_pair_synapses

BINS_NM=(0,25000,50000,100000,200000,500000,1000000,2000000,5000000,10000000,float("inf"))

def load_centroids(path):
    out, inc = {}, {}
    with gzip.open(path,"rt",newline="") as f:
        for r in csv.DictReader(f):
            rid=r["root_id"]
            out[rid]=(float(r["out_x"]),float(r["out_y"]),float(r["out_z"]))
            inc[rid]=(float(r["in_x"]),float(r["in_y"]),float(r["in_z"]))
    return out,inc

def distance_nm(a,b):
    dx=(a[0]-b[0])*4.0; dy=(a[1]-b[1])*4.0; dz=(a[2]-b[2])*40.0
    return math.sqrt(dx*dx+dy*dy+dz*dz)

def dbin(x):
    for i in range(len(BINS_NM)-1):
        if BINS_NM[i] <= x < BINS_NM[i+1]: return i
    raise ValueError(x)

def load_graph(path,min_synapses):
    accepted=set(aggregate_pair_synapses(path,min_synapses=min_synapses))
    outgoing=defaultdict(Counter)
    with _open_csv(path) as fh:
        reader=csv.DictReader(fh)
        s=_pick(reader.fieldnames,SOURCE_CANDIDATES); t=_pick(reader.fieldnames,TARGET_CANDIDATES)
        if "neuropil" not in reader.fieldnames: raise ValueError("input must contain neuropil")
        for row in reader:
            p=(row[s],row[t])
            if p not in accepted: continue
            try: w=int(row["syn_count"])
            except (KeyError,TypeError,ValueError): w=1
            outgoing[p[0]][row["neuropil"]]+=w
    blocks={u:c.most_common(1)[0][0] for u,c in outgoing.items() if c}
    return accepted,blocks

def block_counts(edges,blocks):
    return Counter((blocks[u],blocks[v]) for u,v in edges)

def degree_maps(edges):
    ins,outs=Counter(),Counter()
    for u,v in edges: outs[u]+=1; ins[v]+=1
    return ins,outs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--connections",required=True); ap.add_argument("--centroids",required=True)
    ap.add_argument("--output",required=True); ap.add_argument("--seed",type=int,default=20260935)
    ap.add_argument("--attempts",type=int,default=100000); ap.add_argument("--min-synapses",type=int,default=5)
    args=ap.parse_args()
    outc,inc=load_centroids(Path(args.centroids))
    edges=list(aggregate_pair_synapses(args.connections,min_synapses=args.min_synapses))
    blocks=load_graph(Path(args.connections),args.min_synapses)[1]
    if len(blocks)==0: raise ValueError("no block assignments")
    missing=[e for e in edges if e[0] not in outc or e[1] not in inc or e[0] not in blocks or e[1] not in blocks]
    if missing: raise ValueError(f"coverage incomplete: {len(missing)} edges")
    edge_list=list(edges); edge_set=set(edges)
    edge_bins=[dbin(distance_nm(outc[u],inc[v])) for u,v in edge_list]
    initial_bins=Counter(edge_bins); initial_blocks=block_counts(edge_list,blocks)
    initial_in,initial_out=degree_maps(edge_list)
    constrained_edges=[e for e in edge_list if e[0] in blocks and e[1] in blocks]
    rng=random.Random(args.seed)
    accepted=invalid=block_reject=distance_reject=0
    for _ in range(args.attempts):
        i,j=rng.sample(range(len(edge_list)),2)
        a,b=edge_list[i]; c,d=edge_list[j]
        if a==d or c==b or a==c or b==d:
            invalid+=1; continue
        p1,p2=(a,d),(c,b)
        if p1 in edge_set or p2 in edge_set or p1==p2:
            invalid+=1; continue
        if a not in blocks or b not in blocks or c not in blocks or d not in blocks:
            block_reject+=1; continue
        old_block=sorted(((blocks[a],blocks[b]),(blocks[c],blocks[d])))
        new_block=sorted(((blocks[a],blocks[d]),(blocks[c],blocks[b])))
        if old_block!=new_block:
            block_reject+=1; continue
        old_bin=sorted((edge_bins[i],edge_bins[j]))
        new_bin=sorted((dbin(distance_nm(outc[a],inc[d])),dbin(distance_nm(outc[c],inc[b]))))
        if old_bin!=new_bin:
            distance_reject+=1; continue
        edge_set.remove((a,b)); edge_set.remove((c,d)); edge_set.add(p1); edge_set.add(p2)
        edge_list[i],edge_list[j]=p1,p2; edge_bins[i],edge_bins[j]=new_bin
        accepted+=1
    final_in,final_out=degree_maps(edge_list)
    preservation={
        "same_edge_count":len(edge_set)==len(edges),
        "same_in_degree":initial_in==final_in,
        "same_out_degree":initial_out==final_out,
        "same_block_pair_counts":initial_blocks==block_counts(edge_list,blocks),
        "same_distance_bin_histogram":initial_bins==Counter(edge_bins),
        "no_self_loops":all(u!=v for u,v in edge_list),
        "no_duplicate_edges":len(edge_set)==len(edge_list),
    }
    result={
        "dataset":"FAFB","version":"v783","purpose":"C2 NPC-like + arbor-distance feasibility pilot",
        "attempts":args.attempts,"seed":args.seed,"accepted_swaps":accepted,
        "acceptance_rate":accepted/args.attempts if args.attempts else 0.0,
        "invalid_or_duplicate":invalid,"block_rejected":block_reject,"distance_bin_rejected":distance_reject,
        "unique_directed_pairs":len(edges),"block_count_pairs":len(initial_blocks),
        "distance_bins_nm":list(BINS_NM),"preservation":preservation,
        "all_invariants_preserved":all(preservation.values()),
        "scientific_conclusion":None,
        "interpretation":"feasibility only; no rich-club inference",
        "limitations":["NPC-like block definition follows project implementation","coarse arbor-distance bins are preserved","pilot acceptance does not establish biological mechanism"],
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2))
# C2 pilot bootstrap validation.
if __name__=="__main__": main()
