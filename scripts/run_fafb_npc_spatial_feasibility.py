#!/usr/bin/env python3
"""C2 feasibility pilot: NPC-like block preservation + arbor-distance-bin preservation."""
from __future__ import annotations
import argparse, csv, gzip, json, math, random, bisect, time
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
    # Edges with no dominant block assignment are frozen and excluded from the
    # NPC block-pair constraint; they remain in the full graph and degree maps.
    return Counter((blocks[u],blocks[v]) for u,v in edges if u in blocks and v in blocks)

def degree_maps(edges):
    ins,outs=Counter(),Counter()
    for u,v in edges: outs[u]+=1; ins[v]+=1
    return ins,outs

def build_block_buckets(edge_list,blocks):
    """Index eligible edges by fixed source-block -> target-block class.

    Accepted swaps stay within the selected class, so class sizes remain fixed.
    Sampling pairs from these classes removes proposal attempts that can never
    satisfy the NPC block constraint without changing the constrained state
    space. The distance-bin condition is still checked exactly.
    """
    buckets=defaultdict(list)
    for idx,(u,v) in enumerate(edge_list):
        if u in blocks and v in blocks:
            buckets[(blocks[u],blocks[v])].append(idx)
    eligible_pairs=sum(len(ix)*(len(ix)-1)//2 for ix in buckets.values())
    keys=list(buckets)
    cumulative=[]; total=0
    for key in keys:
        m=len(buckets[key])
        total += m*(m-1)//2
        cumulative.append(total)
    return buckets, keys, cumulative, total

def choose_bucket_pair(rng,buckets,keys,cumulative,total):
    if total <= 0:
        raise ValueError("no eligible block-pair has at least two edges")
    r=rng.randrange(total)
    k=bisect.bisect_right(cumulative,r)
    key=keys[k]
    ix=buckets[key]
    m=len(ix)
    x=rng.randrange(m)
    y=rng.randrange(m-1)
    if y >= x: y += 1
    return ix[x],ix[y]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--connections",required=True); ap.add_argument("--centroids",required=True)
    ap.add_argument("--output",required=True); ap.add_argument("--seed",type=int,default=20260935)
    ap.add_argument("--attempts",type=int,default=100000); ap.add_argument("--min-synapses",type=int,default=5)
    ap.add_argument("--checkpoint-every",type=int,default=100000)
    args=ap.parse_args()
    outc,inc=load_centroids(Path(args.centroids))
    edges=list(aggregate_pair_synapses(args.connections,min_synapses=args.min_synapses))
    blocks=load_graph(Path(args.connections),args.min_synapses)[1]
    if len(blocks)==0: raise ValueError("no block assignments")

    # Arbor centroids are required for every graph edge because distance bins
    # are a global constraint. Missing NPC blocks are not a data-coverage
    # failure: those edges are deliberately frozen for C2.
    missing_centroid=[e for e in edges if e[0] not in outc or e[1] not in inc]
    if missing_centroid:
        raise ValueError(f"arbor-centroid coverage incomplete: {len(missing_centroid)} edges")

    edge_list=list(edges); edge_set=set(edges)
    edge_bins=[dbin(distance_nm(outc[u],inc[v])) for u,v in edge_list]
    initial_bins=Counter(edge_bins); initial_blocks=block_counts(edge_list,blocks)
    initial_in,initial_out=degree_maps(edge_list)
    frozen_block_edges=sum(1 for u,v in edge_list if u not in blocks or v not in blocks)
    buckets,bucket_keys,cumulative,total_pair_choices=build_block_buckets(edge_list,blocks)

    if args.checkpoint_every <= 0:
        raise ValueError("--checkpoint-every must be > 0")

    rng=random.Random(args.seed)
    accepted=invalid=block_reject=distance_reject=0
    checkpoints=[]
    start_time=time.perf_counter()
    for attempt in range(1,args.attempts+1):
        i,j=choose_bucket_pair(rng,buckets,bucket_keys,cumulative,total_pair_choices)
        a,b=edge_list[i]; c,d=edge_list[j]
        if a==d or c==b or a==c or b==d:
            invalid+=1; continue
        p1,p2=(a,d),(c,b)
        if p1 in edge_set or p2 in edge_set or p1==p2:
            invalid+=1; continue
        # The proposal kernel already samples within one source-block -> target-
        # block class. Keep the explicit check as a defensive invariant.
        if blocks.get(a) != blocks.get(c) or blocks.get(b) != blocks.get(d):
            block_reject+=1; continue
        old_bin=sorted((edge_bins[i],edge_bins[j]))
        new_bin=sorted((dbin(distance_nm(outc[a],inc[d])),dbin(distance_nm(outc[c],inc[b]))))
        if old_bin!=new_bin:
            distance_reject+=1; continue
        edge_set.remove((a,b)); edge_set.remove((c,d)); edge_set.add(p1); edge_set.add(p2)
        edge_list[i],edge_list[j]=p1,p2; edge_bins[i],edge_bins[j]=new_bin
        accepted+=1

        if attempt % args.checkpoint_every == 0 or attempt == args.attempts:
            elapsed=time.perf_counter()-start_time
            checkpoints.append({
                "attempts":attempt,
                "accepted_swaps":accepted,
                "acceptance_rate":accepted/attempt if attempt else 0.0,
                "invalid_or_duplicate":invalid,
                "block_rejected":block_reject,
                "distance_bin_rejected":distance_reject,
                "elapsed_seconds":elapsed,
                "attempts_per_second":attempt/elapsed if elapsed > 0 else None,
            })

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
        "proposal_kernel":"block-pair-stratified degree-preserving swap proposal; exact distance-bin acceptance check",
        "attempts":args.attempts,"seed":args.seed,"accepted_swaps":accepted,
        "checkpoint_every":args.checkpoint_every,"checkpoints":checkpoints,
        "acceptance_rate":accepted/args.attempts if args.attempts else 0.0,
        "invalid_or_duplicate":invalid,"block_rejected":block_reject,"distance_bin_rejected":distance_reject,
        "unique_directed_pairs":len(edges),"block_count_pairs":len(initial_blocks),
        "eligible_block_pair_classes":len(buckets),"eligible_pair_choices":total_pair_choices,
        "frozen_edges_without_complete_block_assignment":frozen_block_edges,
        "distance_bins_nm":list(BINS_NM),"preservation":preservation,
        "all_invariants_preserved":all(preservation.values()),
        "scientific_conclusion":None,
        "interpretation":"feasibility only; no rich-club inference",
        "limitations":[
            "NPC-like block definition follows project implementation",
            "edges without complete dominant block assignment are frozen and excluded from the block-pair constraint",
            "proposal is stratified by fixed block-pair class; distance bins remain an exact acceptance constraint",
            "coarse arbor-distance bins are preserved",
            "pilot acceptance does not establish biological mechanism",
        ],
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
