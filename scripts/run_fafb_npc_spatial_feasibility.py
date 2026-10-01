#!/usr/bin/env python3
"""C2 feasibility pilot: NPC-like block preservation + arbor-distance-bin preservation."""
from __future__ import annotations
import argparse, csv, gzip, json, math, random, bisect, time, pickle, hashlib, gc, resource
from collections import Counter, defaultdict
from pathlib import Path
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES, aggregate_pair_synapses
from scripts.run_fafb_rich_club import curve as rich_club_curve

BINS_NM=(0,25000,50000,100000,200000,500000,1000000,2000000,5000000,10000000,float("inf"))

def sha256_file(path, chunk_size=1024*1024):
    h=hashlib.sha256()
    with open(path,"rb") as fh:
        while True:
            chunk=fh.read(chunk_size)
            if not chunk: break
            h.update(chunk)
    return h.hexdigest()

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

def c2_rich_club_curve(observed_edges, null_edges, thresholds=range(20,121)):
    """Compute descriptive observed/null rich-club ratios for one completed C2 null."""
    thresholds=sorted(set(int(k) for k in thresholds))
    observed=rich_club_curve(observed_edges, thresholds)
    null=rich_club_curve(null_edges, thresholds)
    rows=[]
    for o,n in zip(observed,null):
        ratio=(o["rich_density"] / n["rich_density"]
               if n["rich_density"] else None)
        rows.append({**o,
                     "null_rich_density":n["rich_density"],
                     "observed_to_null":ratio,
                     "phi_norm":ratio,
                     "above_1pct":bool(ratio is not None and ratio > 1.01)})
    above=[r["threshold"] for r in rows if r["above_1pct"]]
    return {
        "thresholds":thresholds,
        "curve":rows,
        "rich_club_criterion":"phi_norm > 1.01",
        "onset_threshold":min(above) if above else None,
        "offset_threshold":max(above) if above else None,
        "peak_threshold":max(rows,key=lambda r: r["phi_norm"] if r["phi_norm"] is not None else float("-inf"))["threshold"] if rows else None,
        "null_count":1,
        "interpretation":"descriptive single-null comparison; not a significance test",
    }

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

def save_c2_state(path, state, compresslevel=1):
    """Persist a resumable C2 state with low-overhead gzip compression.

    The checkpoint is dominated by the 3.7M-edge edge_list. Level-1 gzip is
    intentional: checkpoints are recovery artifacts, not archival artifacts.
    The atomic tmp->replace sequence prevents a partial checkpoint from being
    mistaken for a valid resume state after interruption.
    """
    path=Path(path)
    tmp_path=Path(str(path)+".tmp")
    with gzip.open(tmp_path,"wb",compresslevel=compresslevel) as fh:
        pickle.dump(state,fh,protocol=pickle.HIGHEST_PROTOCOL)
    tmp_path.replace(path)


def load_c2_state(path):
    with gzip.open(path,"rb") as fh:
        return pickle.load(fh)


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--connections",required=True); ap.add_argument("--centroids",required=True)
    ap.add_argument("--output",required=True); ap.add_argument("--seed",type=int,default=20260935)
    ap.add_argument("--attempts",type=int,default=100000); ap.add_argument("--target-accepted",type=int,default=0); ap.add_argument("--min-synapses",type=int,default=5)
    ap.add_argument("--checkpoint-every",type=int,default=100000)
    ap.add_argument("--checkpoint-seconds",type=float,default=120.0)
    ap.add_argument("--resume-state",default="")
    ap.add_argument("--code-version",default="unknown")
    ap.add_argument("--allow-resume-code-version-mismatch",action="store_true")
    ap.add_argument("--input-fingerprint",default="unknown")
    args=ap.parse_args()
    outc,inc=load_centroids(Path(args.centroids))
    edges=list(aggregate_pair_synapses(args.connections,min_synapses=args.min_synapses))
    blocks=load_graph(Path(args.connections),args.min_synapses)[1]
    if len(blocks)==0: raise ValueError("no block assignments")

    # Arbor centroids are required for every graph edge because distance bins
    # are a global constraint. Missing NPC blocks are not a data-coverage
    # failure: those edges are deliberately frozen for C2.
    missing_centroid=sum(1 for u,v in edges if u not in outc or v not in inc)
    if missing_centroid:
        raise ValueError(f"arbor-centroid coverage incomplete: {missing_centroid} edges")

    # Keep the authoritative observed graph as the immutable baseline. On resume,
    # do not build a second mutable edge_list/bucket index before loading the
    # checkpoint; that duplication was causing severe memory pressure.
    initial_bins=Counter(dbin(distance_nm(outc[u],inc[v])) for u,v in edges)
    initial_blocks=block_counts(edges,blocks)
    initial_in,initial_out=degree_maps(edges)
    input_fingerprint=args.input_fingerprint
    constraint_payload=json.dumps({
        "dataset":"FAFB", "version":"v783", "min_synapses":args.min_synapses,
        "distance_bins_nm":list(BINS_NM), "input_fingerprint":input_fingerprint,
        "unique_directed_pairs":len(edges),
        "block_count_pairs":len(initial_blocks),
    }, sort_keys=True, separators=(",",":"))
    constraint_fingerprint=hashlib.sha256(constraint_payload.encode("utf-8")).hexdigest()
    frozen_block_edges=sum(1 for u,v in edges if u not in blocks or v not in blocks)

    if args.checkpoint_every <= 0:
        raise ValueError("--checkpoint-every must be > 0")
    if args.checkpoint_seconds <= 0:
        raise ValueError("--checkpoint-seconds must be > 0")

    rng=random.Random(args.seed)
    accepted=invalid=block_reject=distance_reject=0
    checkpoints=[]
    attempt=0
    if args.resume_state:
        state=load_c2_state(args.resume_state)
        if state.get("seed") != args.seed:
            raise ValueError("resume state seed does not match --seed")
        resume_code_version=state.get("code_version")
        if resume_code_version != args.code_version:
            if not args.allow_resume_code_version_mismatch:
                raise ValueError("resume state code version does not match --code-version")
            print(json.dumps({
                "resume_code_version_migration": {
                    "from": resume_code_version,
                    "to": args.code_version,
                    "reason": "checkpoint-only infrastructure change; constraint fingerprint remains mandatory",
                }
            }), flush=True)
        if state.get("constraint_fingerprint") != constraint_fingerprint:
            raise ValueError("resume state constraint fingerprint does not match current inputs")
        edge_list=state["edge_list"]
        edge_bins=state["edge_bins"]
        accepted=int(state["accepted"])
        invalid=int(state["invalid"])
        block_reject=int(state["block_reject"])
        distance_reject=int(state["distance_reject"])
        attempt=int(state["attempt"])
        rng.setstate(state["rng_state"])
        checkpoints=list(state.get("checkpoints", []))
        edge_set=set(edge_list)
        if len(edge_list) != len(edges) or len(edge_set) != len(edge_list):
            raise ValueError("resume state edge count/uniqueness mismatch")
        if Counter(edge_bins) != initial_bins:
            raise ValueError("resume state distance-bin histogram mismatch")
        if degree_maps(edge_list) != (initial_in, initial_out):
            raise ValueError("resume state degree maps mismatch")
        if block_counts(edge_list,blocks) != initial_blocks:
            raise ValueError("resume state block-pair counts mismatch")
        print(json.dumps({"resumed_from_attempt":attempt,"accepted_swaps":accepted,"resume_rss_max_mb_before_release":rss_mb()}), flush=True)
        del state
        gc.collect()
        print(json.dumps({"resume_state_released":True,"resume_rss_max_mb_after_release":rss_mb(),"edge_list_len":len(edge_list),"edge_set_len":len(edge_set),"edge_bins_len":len(edge_bins)}), flush=True)
    # Build the proposal buckets only after the final mutable edge_list has been
    # selected. This avoids retaining a bucket index tied to the pre-resume graph
    # alongside the resumed state.
    if not args.resume_state:
        edge_list=list(edges)
        edge_bins=[dbin(distance_nm(outc[u],inc[v])) for u,v in edge_list]
        edge_set=set(edge_list)
    buckets,bucket_keys,cumulative,total_pair_choices=build_block_buckets(edge_list,blocks)

    start_time=time.perf_counter()
    last_checkpoint_elapsed=0.0
    last_heartbeat_elapsed=0.0

    def current_rss_mb():
        try:
            text=Path("/proc/self/status").read_text()
            return int(text.split("VmRSS:",1)[1].split("kB",1)[0].strip()) / 1024.0
        except (FileNotFoundError,IndexError,ValueError):
            return None

    def maybe_checkpoint(force=False):
        nonlocal last_checkpoint_elapsed
        elapsed=time.perf_counter()-start_time
        due_by_attempt=(attempt % args.checkpoint_every == 0 or attempt == args.attempts)
        due_by_time=(elapsed-last_checkpoint_elapsed) >= args.checkpoint_seconds
        if not force and not due_by_attempt and not due_by_time:
            return
        if not checkpoints or checkpoints[-1]["attempts"] != attempt:
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
        state={
            "version":2,
            "seed":args.seed,
            "code_version":args.code_version,
            "constraint_fingerprint":constraint_fingerprint,
            "attempt":attempt,
            "accepted":accepted,
            "invalid":invalid,
            "block_reject":block_reject,
            "distance_reject":distance_reject,
            "edge_list":edge_list,
            "edge_bins":edge_bins,
            "rng_state":rng.getstate(),
            "checkpoints":checkpoints,
        }
        state_path=Path(args.output).with_name("c2-state.pkl.gz")
        save_c2_state(state_path,state)
        last_checkpoint_elapsed=elapsed
        print(
            f"attempt={attempt} accepted={accepted} "
            f"rate={accepted/attempt:.4%}",
            flush=True,
        )

    if args.resume_state:
        maybe_checkpoint(force=True)

    while attempt < args.attempts and (args.target_accepted <= 0 or accepted < args.target_accepted):
        attempt += 1
        heartbeat_elapsed=time.perf_counter()-start_time
        if heartbeat_elapsed-last_heartbeat_elapsed >= 10.0:
            rate=attempt/heartbeat_elapsed if heartbeat_elapsed > 0 else 0.0
            print(json.dumps({"heartbeat":"before_proposal","attempt":attempt,"accepted_swaps":accepted,"elapsed_seconds":heartbeat_elapsed,"attempts_per_second":rate,"rss_current_mb":current_rss_mb(),"rss_max_mb":rss_mb()}), flush=True)
            last_heartbeat_elapsed=heartbeat_elapsed
        proposal_started=time.perf_counter()
        proposal_rss_before=current_rss_mb()
        print(json.dumps({"proposal_start":True,"attempt":attempt,"accepted_swaps":accepted,"rss_current_mb":proposal_rss_before,"rss_max_mb":rss_mb()}), flush=True)
        i,j=choose_bucket_pair(rng,buckets,bucket_keys,cumulative,total_pair_choices)
        proposal_elapsed=time.perf_counter()-proposal_started
        print(json.dumps({"proposal_end":True,"attempt":attempt,"accepted_swaps":accepted,"proposal_seconds":proposal_elapsed,"rss_current_mb":current_rss_mb(),"rss_max_mb":rss_mb()}), flush=True)
        if proposal_elapsed >= 5.0:
            print(json.dumps({"slow_proposal_seconds":proposal_elapsed,"attempt":attempt,"accepted_swaps":accepted,"rss_current_mb":current_rss_mb(),"rss_max_mb":rss_mb()}), flush=True)
        a,b=edge_list[i]; c,d=edge_list[j]
        if a==d or c==b or a==c or b==d:
            invalid+=1; maybe_checkpoint(); continue
        p1,p2=(a,d),(c,b)
        if p1 in edge_set or p2 in edge_set or p1==p2:
            invalid+=1; maybe_checkpoint(); continue
        # The proposal kernel already samples within one source-block -> target-
        # block class. Keep the explicit check as a defensive invariant.
        if blocks.get(a) != blocks.get(c) or blocks.get(b) != blocks.get(d):
            block_reject+=1; maybe_checkpoint(); continue
        old_bin=sorted((edge_bins[i],edge_bins[j]))
        new_bin=sorted((dbin(distance_nm(outc[a],inc[d])),dbin(distance_nm(outc[c],inc[b]))))
        if old_bin!=new_bin:
            distance_reject+=1; maybe_checkpoint(); continue
        edge_set.remove((a,b)); edge_set.remove((c,d)); edge_set.add(p1); edge_set.add(p2)
        edge_list[i],edge_list[j]=p1,p2; edge_bins[i],edge_bins[j]=new_bin
        accepted+=1
        maybe_checkpoint()

    final_in,final_out=degree_maps(edge_list)
    final_edges=set(edge_list)
    rich_club=c2_rich_club_curve(set(edges),final_edges)
    original_edge_overlap_fraction=sum(1 for e in final_edges if e in edges) / len(edges) if edges else 0.0
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
        "attempts":attempt,"target_accepted":args.target_accepted,"seed":args.seed,"accepted_swaps":accepted,
        "code_version":args.code_version,"input_fingerprint":input_fingerprint,"constraint_fingerprint":constraint_fingerprint,
        "checkpoint_every":args.checkpoint_every,"checkpoint_seconds":args.checkpoint_seconds,"checkpoints":checkpoints,
        "acceptance_rate":accepted/attempt if attempt else 0.0,
        "invalid_or_duplicate":invalid,"block_rejected":block_reject,"distance_bin_rejected":distance_reject,
        "unique_directed_pairs":len(edges),"block_count_pairs":len(initial_blocks),
        "eligible_block_pair_classes":len(buckets),"eligible_pair_choices":total_pair_choices,
        "frozen_edges_without_complete_block_assignment":frozen_block_edges,
        "distance_bins_nm":list(BINS_NM),"preservation":preservation,
        "all_invariants_preserved":all(preservation.values()),
        "target_reached": (args.target_accepted <= 0 or accepted >= args.target_accepted),
        "rich_club":rich_club,
        "original_edge_overlap_fraction":original_edge_overlap_fraction,
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
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
