#!/usr/bin/env python3
"""Synthetic C2 positive-control / power experiment."""
from __future__ import annotations
import argparse, json, random
from collections import Counter, defaultdict
from pathlib import Path

def distance_bin(u: int, v: int, n_bins: int = 3) -> int:
    if u == v: raise ValueError("self-loop has no distance bin")
    return ((abs(u-v)//10)+((u*17+v*31)%n_bins))%n_bins

def build_base_graph(n: int, edge_probability: float, seed: int):
    rng=random.Random(seed); blocks={u:u%2 for u in range(n)}
    edges={(u,v) for u in range(n) for v in range(n) if u!=v and rng.random()<edge_probability}
    return edges,blocks

def degree_maps(edges):
    indegree=Counter(); outdegree=Counter()
    for u,v in edges: outdegree[u]+=1; indegree[v]+=1
    nodes=set(indegree)|set(outdegree)
    return indegree,outdegree,{u:indegree[u]+outdegree[u] for u in nodes}

def constraint_signature(edges,blocks):
    bp=Counter((blocks[u],blocks[v]) for u,v in edges)
    db=Counter(distance_bin(u,v) for u,v in edges)
    indegree,outdegree,_=degree_maps(edges)
    block_pair_counts={f"{a}->{b}":count for (a,b),count in sorted(bp.items())}
    return {"edge_count":len(edges),"in_degree":dict(sorted(indegree.items())),
            "out_degree":dict(sorted(outdegree.items())),
            "block_pair_counts":block_pair_counts,
            "distance_bin_counts":dict(sorted(db.items())),
            "no_self_loops":all(u!=v for u,v in edges),
            "no_duplicate_edges":len(edges)==len(set(edges))}

def choose_c2_swap(edges,blocks,rng):
    buckets=defaultdict(list)
    for edge in edges: buckets[(blocks[edge[0]],blocks[edge[1]])].append(edge)
    eligible=[k for k,v in buckets.items() if len(v)>=2]
    if not eligible: return None
    e1,e2=rng.sample(buckets[rng.choice(eligible)],2); a,b=e1; c,d=e2
    if a==d or c==b or a==c or b==d: return None
    p1,p2=(a,d),(c,b)
    if p1 in edges or p2 in edges or p1==p2: return None
    if blocks[a]!=blocks[c] or blocks[b]!=blocks[d]: return None
    if sorted((distance_bin(*e1),distance_bin(*e2))) != sorted((distance_bin(*p1),distance_bin(*p2))): return None
    return e1,e2,p1,p2

def apply_swap(edges,proposal):
    e1,e2,p1,p2=proposal; edges.remove(e1); edges.remove(e2); edges.add(p1); edges.add(p2)

def club_edge_count(edges,club): return sum(u in club and v in club for u,v in edges)

def fixed_club_curve(observed,null_edges,thresholds):
    _,_,degrees=degree_maps(observed); rows=[]
    for threshold in thresholds:
        club={u for u,d in degrees.items() if d>=threshold}; possible=len(club)*(len(club)-1)
        oe=club_edge_count(observed,club); ne=club_edge_count(null_edges,club)
        od=oe/possible if possible else None; nd=ne/possible if possible else None
        phi=od/nd if od is not None and nd else None
        rows.append({"threshold":threshold,"fixed_club_size":len(club),
                     "observed_club_edges":oe,"null_club_edges":ne,
                     "observed_density":od,"null_density":nd,
                     "phi_norm_fixed_club":phi,"above_1_01":bool(phi is not None and phi>1.01)})
    return rows

def plant_rich_club(edges,blocks,club,target_gain,seed,max_attempts):
    rng=random.Random(seed); start=club_edge_count(edges,club); accepted=0
    for attempt in range(1,max_attempts+1):
        proposal=choose_c2_swap(edges,blocks,rng)
        if proposal is None: continue
        e1,e2,p1,p2=proposal
        before=sum(u in club and v in club for u,v in (e1,e2))
        after=sum(u in club and v in club for u,v in (p1,p2))
        if after>before:
            apply_swap(edges,proposal); accepted+=1
            if club_edge_count(edges,club)>=start+target_gain: return attempt,accepted,start
    raise RuntimeError(f"could not plant target gain {target_gain}; start={start} final={club_edge_count(edges,club)}")

def run_null(observed,blocks,club,attempts,seed):
    rng=random.Random(seed); edges=set(observed); accepted=0
    for _ in range(attempts):
        proposal=choose_c2_swap(edges,blocks,rng)
        if proposal is not None: apply_swap(edges,proposal); accepted+=1
    return edges,accepted,club_edge_count(edges,club)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nodes",type=int,default=80); ap.add_argument("--edge-probability",type=float,default=0.18)
    ap.add_argument("--club-size",type=int,default=12); ap.add_argument("--plant-gain",type=int,default=50)
    ap.add_argument("--plant-seed",type=int,default=7); ap.add_argument("--base-seed",type=int,default=1)
    ap.add_argument("--null-attempts",type=int,default=100000); ap.add_argument("--null-seeds",default="101,102,103")
    ap.add_argument("--max-plant-attempts",type=int,default=500000)
    ap.add_argument("--output",default="artifacts/c2-positive-control/result.json"); args=ap.parse_args()
    base,blocks=build_base_graph(args.nodes,args.edge_probability,args.base_seed)
    _,_,base_degrees=degree_maps(base)
    club=set(sorted(base_degrees,key=lambda u:(base_degrees[u],u),reverse=True)[:args.club_size])
    planted=set(base)
    plant_attempts,plant_accepts,base_club_edges=plant_rich_club(planted,blocks,club,args.plant_gain,args.plant_seed,args.max_plant_attempts)
    before_signature=constraint_signature(base,blocks); planted_signature=constraint_signature(planted,blocks)
    if before_signature!=planted_signature: raise AssertionError("planting changed a preserved C2 statistic")
    planted_club_edges=club_edge_count(planted,club); thresholds=list(range(20,41)); null_results=[]
    for seed_text in args.null_seeds.split(","):
        seed=int(seed_text.strip()); null_edges,accepted,final_club_edges=run_null(planted,blocks,club,args.null_attempts,seed)
        if planted_signature!=constraint_signature(null_edges,blocks): raise AssertionError(f"null seed {seed} violated a C2 invariant")
        curve=fixed_club_curve(planted,null_edges,thresholds)
        valid=[r["phi_norm_fixed_club"] for r in curve if r["phi_norm_fixed_club"] is not None]
        null_results.append({"seed":seed,"attempts":args.null_attempts,"accepted_swaps":accepted,
            "final_fixed_club_edges":final_club_edges,
            "final_fixed_club_fraction_of_planted":final_club_edges/planted_club_edges,
            "curve":curve,"peak_phi_norm_fixed_club":max(valid) if valid else None,
            "peak_threshold":max((r for r in curve if r["phi_norm_fixed_club"] is not None),
                                 key=lambda r:r["phi_norm_fixed_club"])["threshold"] if valid else None})
    all_pass=all(r["final_fixed_club_edges"]<planted_club_edges and any(x["above_1_01"] for x in r["curve"]) for r in null_results)
    result={"experiment":"C2 synthetic positive-control / power","scientific_status":"synthetic control only; no FAFB inference",
        "parameters":vars(args),
        "construction":{"source_target_blocks":"2 blocks; block(u)=u mod 2","distance_bins":"3 deterministic pairwise bins independent of planted club membership",
            "club_definition":"fixed from highest total degree in the unplanted base graph",
            "planting":"strictly C2-valid swaps selected only when they increase fixed-club internal edges"},
        "base":{"constraint_signature":before_signature,"club":sorted(club),"base_fixed_club_edges":base_club_edges},
        "planted":{"constraint_signature":planted_signature,"plant_attempts":plant_attempts,"plant_accepted_swaps":plant_accepts,
            "fixed_club_edges":planted_club_edges,"gain":planted_club_edges-base_club_edges},
        "nulls":null_results,"power_pass":all_pass,
        "acceptance_criteria":{"fixed_club_membership":True,"preserved_c2_statistics":True,
            "nulls_reduce_planted_signal":all_pass,"multiple_seeds":len(null_results)>=3,
            "complete_fixed_membership_curve_separates":all(any(x["above_1_01"] for x in r["curve"]) for r in null_results)},
        "interpretation":"A pass demonstrates detectability of a synthetic signal under the C2 constraint geometry. It does not establish a biological effect or close Gate C."}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))

if __name__=="__main__": main()
