#!/usr/bin/env python3
"""FAFB v783 rich-club null constrained by degree and dominant outgoing neuropil."""
from __future__ import annotations
import argparse, csv, json, random
from pathlib import Path
from collections import Counter, defaultdict
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES

def load_graph(path):
    edges=set(); outgoing=defaultdict(Counter)
    with _open_csv(path) as fh:
        reader=csv.DictReader(fh)
        s=_pick(reader.fieldnames,SOURCE_CANDIDATES); t=_pick(reader.fieldnames,TARGET_CANDIDATES)
        if "neuropil" not in reader.fieldnames: raise ValueError("input must contain neuropil")
        for row in reader:
            u,v=row[s],row[t]
            if u==v: continue
            edges.add((u,v))
            try: w=int(row["syn_count"])
            except (KeyError,TypeError,ValueError): w=1
            outgoing[u][row["neuropil"]]+=w
    blocks={u:c.most_common(1)[0][0] for u,c in outgoing.items() if c}
    return edges,blocks

def constrained_randomization(edges,blocks,swaps,seed):
    current=set(edges); edge_list=list(current); rng=random.Random(seed)
    successful=attempts=0; max_attempts=max(100,swaps*50)
    while successful<swaps and attempts<max_attempts:
        attempts+=1; i,j=rng.sample(range(len(edge_list)),2)
        a,b=edge_list[i]; c,d=edge_list[j]
        if blocks.get(a)!=blocks.get(c) or blocks.get(b)!=blocks.get(d): continue
        if a==d or c==b: continue
        n1,n2=(a,d),(c,b)
        if n1==n2 or n1 in current or n2 in current: continue
        current.remove((a,b)); current.remove((c,d)); current.add(n1); current.add(n2)
        edge_list[i],edge_list[j]=n1,n2; successful+=1
    return current,successful,attempts

def degree_report(a,b):
    def seq(edges):
        ins=Counter(); outs=Counter()
        for u,v in edges: outs[u]+=1; ins[v]+=1
        return ins,outs
    ai,ao=seq(a); bi,bo=seq(b); nodes=set(ai)|set(ao)|set(bi)|set(bo)
    return {"same_edge_count":len(a)==len(b),"same_in_degree":all(ai[n]==bi[n] for n in nodes),
            "same_out_degree":all(ao[n]==bo[n] for n in nodes)}

def block_counts(edges,blocks):
    return Counter((blocks[u],blocks[v]) for u,v in edges if u in blocks and v in blocks)

def curve(edges,thresholds):
    ins=Counter(); outs=Counter()
    for u,v in edges: outs[u]+=1; ins[v]+=1
    nodes=set(ins)|set(outs); deg={u:ins[u]+outs[u] for u in nodes}; out=[]
    for k in thresholds:
        rich={u for u,d in deg.items() if d>=k}; possible=len(rich)*(len(rich)-1)
        re=sum(1 for u,v in edges if u in rich and v in rich)
        out.append({"threshold":k,"rich_nodes":len(rich),"rich_edges":re,
                    "rich_density":re/possible if possible else 0.0})
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/rich-club-npc.json")
    ap.add_argument("--nulls",type=int,default=8); ap.add_argument("--swaps-per-edge",type=float,default=1.0)
    args=ap.parse_args()
    edges,blocks=load_graph(Path(args.input)); ins=Counter(); outs=Counter()
    for u,v in edges: outs[u]+=1; ins[v]+=1
    vals=[ins[u]+outs[u] for u in set(ins)|set(outs)]
    thresholds=sorted(set(max(1,int(vals[int((len(vals)-1)*q)])) for q in (0.90,0.95,0.99,0.995)))
    observed=curve(edges,thresholds); observed_blocks=block_counts(edges,blocks)
    target=max(1000,int(len(edges)*args.swaps_per_edge)); nulls=[]; reports=[]; block_reports=[]
    for seed in range(args.nulls):
        null,successful,attempts=constrained_randomization(edges,blocks,target,seed)
        nulls.append(curve(null,thresholds))
        reports.append({**degree_report(edges,null),"successful_swaps":successful,"attempts":attempts,"target_swaps":target})
        block_reports.append({"same_block_counts":block_counts(null,blocks)==observed_blocks,
                              "observed_blocks":len(observed_blocks)})
    rows=[]
    for i,o in enumerate(observed):
        nd=[x[i]["rich_density"] for x in nulls]; mean=sum(nd)/len(nd)
        sd=(sum((x-mean)**2 for x in nd)/(len(nd)-1))**0.5 if len(nd)>1 else None
        rows.append({**o,"null_mean_density":mean,"null_sd_density":sd,
                     "observed_to_null":o["rich_density"]/mean if mean else None})
    result={"dataset":"FAFB","version":"v783","unique_directed_pairs":len(edges),
            "block_definition":"dominant outgoing-synapse neuropil per neuron",
            "null_model":"directed degree-preserving swaps preserving source-neuropil -> target-neuropil block counts",
            "nulls":args.nulls,"target_swaps_per_null":target,"thresholds":thresholds,
            "degree_preservation":reports,"block_preservation":block_reports,"curve":rows}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))

if __name__=="__main__": main()
