#!/usr/bin/env python3
"""Sample directed 3-node motif signatures in FAFB and compare degree-preserving nulls."""
from __future__ import annotations
import argparse,csv,json,random
from collections import Counter,defaultdict
from pathlib import Path
from src.graph.connections import _open_csv,_pick,SOURCE_CANDIDATES,TARGET_CANDIDATES
from src.graph.random_baseline import degree_preserving_randomization,degree_preservation_report

def load(path):
    edges=set()
    with _open_csv(path) as fh:
        r=csv.DictReader(fh); s=_pick(r.fieldnames,SOURCE_CANDIDATES); t=_pick(r.fieldnames,TARGET_CANDIDATES)
        for row in r:
            u,v=row[s],row[t]
            if u!=v: edges.add((u,v))
    adj=defaultdict(set)
    for u,v in edges: adj[u].add(v)
    return edges,adj


TRIAD_REPRESENTATIVES = {
    "003": (), "012": ((0,1),), "102": ((0,1),(1,0)),
    "021D": ((1,0),(1,2)), "021U": ((0,1),(2,1)), "021C": ((0,1),(1,2)),
    "111D": ((0,1),(1,0),(2,1)), "111U": ((0,1),(1,0),(1,2)),
    "030T": ((0,1),(1,2),(0,2)), "030C": ((1,0),(2,1),(0,2)),
    "201": ((0,1),(1,0),(1,2),(2,1)),
    "120D": ((1,0),(1,2),(0,2),(2,0)),
    "120U": ((0,1),(2,1),(0,2),(2,0)),
    "120C": ((0,1),(1,2),(0,2),(2,0)),
    "210": ((0,1),(1,0),(1,2),(2,1),(0,2)),
    "300": ((0,1),(1,0),(0,2),(2,0),(1,2),(2,1)),
}
def _sig_pairs(pairs):
    order=((0,1),(1,0),(0,2),(2,0),(1,2),(2,1))
    return sum(1<<i for i,p in enumerate(order) if p in pairs)
TRIAD_SIGNATURE_TO_LABEL={}
for _label,_pairs in TRIAD_REPRESENTATIVES.items():
    _sigs=[]
    for _perm in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
        _mapped={(_perm.index(u),_perm.index(v)) for u,v in _pairs}
        _sigs.append(_sig_pairs(_mapped))
    TRIAD_SIGNATURE_TO_LABEL[min(_sigs)]=_label
def canonical_triad_class(a,b,c,edges):
    nodes=(a,b,c); sigs=[]
    for perm in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
        ordered=tuple(nodes[i] for i in perm)
        sigs.append(signature(*ordered,edges))
    return TRIAD_SIGNATURE_TO_LABEL[min(sigs)]

def signature(a,b,c,e):
    return sum(1<<i for i,p in enumerate(((a,b),(b,a),(a,c),(c,a),(b,c),(c,b))) if p in e)

def sample(edges,adj,n,seed):
    rng=random.Random(seed); nodes=list(adj); counts=Counter(); accepted=0
    if not nodes: return counts,0
    for _ in range(n):
        a=rng.choice(nodes)
        if len(adj[a])<2: continue
        b,c=rng.sample(tuple(adj[a]),2)
        if len({a,b,c})<3: continue
        counts[canonical_triad_class(a,b,c,edges)] += 1; accepted += 1
    return counts,accepted

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/motif-sample.json")
    ap.add_argument("--samples",type=int,default=1000000)
    ap.add_argument("--nulls",type=int,default=4)
    ap.add_argument("--seed",type=int,default=0)
    args=ap.parse_args()
    edges,adj=load(Path(args.input))
    obs,nobs=sample(edges,adj,args.samples,args.seed)
    nulls=[]; swaps=max(1000,int(len(edges)))
    for s in range(args.nulls):
        ne=degree_preserving_randomization(edges,swaps=swaps,seed=s)
        na=defaultdict(set)
        for u,v in ne: na[u].add(v)
        c,n=sample(ne,na,args.samples,args.seed+s+1)
        nulls.append({"counts":dict(c),"accepted":n,"preservation":degree_preservation_report(edges,ne)})
    result={"dataset":"FAFB","version":"v783","unique_directed_pairs":len(edges),
      "sample_count":args.samples,"observed_accepted":nobs,"nulls":nulls,
      "signature_definition":"six directed edge bits on a sampled 3-node wedge; this is a transparent signature, not an isomorphism-class label.",
      "observed_counts":dict(obs)}
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
