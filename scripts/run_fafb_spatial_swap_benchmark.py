#!/usr/bin/env python3
"""Benchmark hard spatial degree-preserving swaps for Gate C1.

A proposed directed two-edge swap (a,b),(c,d)->(a,d),(c,b) is accepted
only when it preserves the multiset of coarse arbor-distance bins of the
two replaced edges. This is a feasibility benchmark, not a scientific
rich-club result.
"""
from __future__ import annotations
import argparse,csv,gzip,json,math,random
from collections import Counter
from pathlib import Path
from src.graph.connections import aggregate_pair_synapses

BINS_NM=(0,25_000,50_000,100_000,200_000,500_000,1_000_000,2_000_000,5_000_000,10_000_000,float("inf"))

def load_centroids(path):
    out={}; inc={}
    with gzip.open(path,"rt",newline="") as f:
        r=csv.DictReader(f)
        for row in r:
            rid=row["root_id"]
            out[rid]=(float(row["out_x"]),float(row["out_y"]),float(row["out_z"]))
            inc[rid]=(float(row["in_x"]),float(row["in_y"]),float(row["in_z"]))
    return out,inc

def distance(a,b):
    dx=(a[0]-b[0])*4.; dy=(a[1]-b[1])*4.; dz=(a[2]-b[2])*40.
    return math.sqrt(dx*dx+dy*dy+dz*dz)

def dbin(x):
    for i in range(len(BINS_NM)-1):
        if BINS_NM[i] <= x < BINS_NM[i+1]: return i
    raise ValueError(x)

def degree_maps(edges):
    indeg=Counter(); outdeg=Counter()
    for u,v in edges:
        outdeg[u]+=1; indeg[v]+=1
    return indeg,outdeg

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--connections",required=True)
    ap.add_argument("--centroids",required=True)
    ap.add_argument("--attempts",type=int,default=100000)
    ap.add_argument("--seed",type=int,default=20260927)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    outc,inc=load_centroids(Path(a.centroids))
    edges_counter=aggregate_pair_synapses(a.connections,min_synapses=5)
    full_edges=list(edges_counter)
    full_nodes={u for u,v in full_edges}|{v for u,v in full_edges}
    edges=[(u,v) for u,v in full_edges if u in outc and v in inc]
    edge_set=set(edges)
    nodes={u for u,v in edges}|{v for u,v in edges}
    dropped_edges=len(full_edges)-len(edges)
    rng=random.Random(a.seed)
    edge_bins=[dbin(distance(outc[u],inc[v])) for u,v in edges]
    initial_bins=Counter(edge_bins)
    indeg0,outdeg0=degree_maps(edges)
    accepted=0; invalid=0; bin_reject=0
    for _ in range(a.attempts):
        i,j=rng.sample(range(len(edges)),2)
        a1,b1=edges[i]; a2,b2=edges[j]
        if a1==b2 or a2==b1 or a1==a2 or b1==b2:
            invalid+=1; continue
        p1=(a1,b2); p2=(a2,b1)
        if p1 in edge_set or p2 in edge_set:
            invalid+=1; continue
        old_bins=sorted((edge_bins[i],edge_bins[j]))
        new_bins=sorted((dbin(distance(outc[a1],inc[b2])),dbin(distance(outc[a2],inc[b1]))))
        if old_bins != new_bins:
            bin_reject+=1; continue
        edge_set.remove((a1,b1)); edge_set.remove((a2,b2))
        edge_set.add(p1); edge_set.add(p2)
        edges[i]=p1; edges[j]=p2
        edge_bins[i],edge_bins[j]=new_bins
        accepted+=1
    indeg1,outdeg1=degree_maps(edges)
    result={
      "purpose":"Gate C1 hard spatial degree-preserving swap feasibility benchmark; no rich-club inference",
      "method":{"swap":"(a,b),(c,d)->(a,d),(c,b)","hard_constraint":"multiset of coarse arbor-distance bins preserved per accepted swap",
        "distance_bins_nm":list(BINS_NM),"distance":"anisotropic Euclidean from outgoing centroid of source to incoming centroid of target"},
      "network":{"full_nodes":len(full_nodes),"full_edges":len(full_edges),"covered_nodes":len(nodes),"covered_edges":len(edges),"dropped_edges_for_coverage":dropped_edges,"node_coverage":len(nodes)/len(full_nodes) if full_nodes else 0.0,"edge_coverage":len(edges)/len(full_edges) if full_edges else 0.0,"min_synapses":5},
      "benchmark":{"seed":a.seed,"attempts":a.attempts,"accepted":accepted,"invalid_or_duplicate":invalid,
        "distance_bin_rejected":bin_reject,"acceptance_rate":accepted/a.attempts if a.attempts else 0.0,
        "edge_count_preserved":len(edges)==len(edge_set),
        "in_degree_preserved":indeg0==indeg1,"out_degree_preserved":outdeg0==outdeg1,
        "distance_bin_histogram_preserved":initial_bins==Counter(edge_bins)},
      "scientific_conclusion":None,
      "next_step":"Covered-subgraph feasibility only; a full-graph spatial null requires a validated coverage strategy and this benchmark is not a rich-club result."
    }
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":main()
