#!/usr/bin/env python3
"""FAFB v783 Princeton synapse-table arbor-aware spatial preflight (Gate C0)."""
from __future__ import annotations
import argparse,csv,gzip,hashlib,json,math,random
from collections import defaultdict
from pathlib import Path
from src.graph.connections import aggregate_pair_synapses

PREFIX="720575940"

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def root_id(raw):
    s=str(raw).strip()
    if not s:return None
    if s.startswith(PREFIX): return s
    if len(s)<=9: return PREFIX+s.zfill(9)
    return s

def dist(a,b):
    dx=(a[0]-b[0])*4.0; dy=(a[1]-b[1])*4.0; dz=(a[2]-b[2])*40.0
    return math.sqrt(dx*dx+dy*dy+dz*dz)

def quant(v):
    if not v:return {}
    x=sorted(v)
    def q(p):return x[min(len(x)-1,int(round(p*(len(x)-1))))]
    return {"min_nm":x[0],"q25_nm":q(.25),"median_nm":q(.5),"q75_nm":q(.75),
            "q90_nm":q(.9),"q95_nm":q(.95),"q99_nm":q(.99),"max_nm":x[-1],
            "mean_nm":sum(x)/len(x)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--connections",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--synapse-table",default="data/raw/fafb_v783/fafb_v783_princeton_synapse_table.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/princeton-arbor-spatial-preflight.json")
    ap.add_argument("--centroids-output",default="artifacts/fafb-v783/arbor-centroids.csv.gz")
    ap.add_argument("--min-synapses",type=int,default=5)
    ap.add_argument("--edge-sample",type=int,default=100000)
    ap.add_argument("--nonedge-sample",type=int,default=100000)
    ap.add_argument("--seed",type=int,default=20260927)
    a=ap.parse_args()
    sp=Path(a.synapse_table); ep=Path(a.connections)
    sums_out=defaultdict(lambda:[0.0,0.0,0.0,0])
    sums_in=defaultdict(lambda:[0.0,0.0,0.0,0])
    rows=0; malformed=0; prefix_counts=set()
    with gzip.open(sp,"rt",newline="") as fh:
        r=csv.DictReader(fh)
        required={"pre_x","pre_y","pre_z","post_x","post_y","post_z","pre_root_id_720575940","post_root_id_720575940"}
        missing=required-set(r.fieldnames or [])
        if missing: raise ValueError(f"missing required columns: {sorted(missing)}")
        for row in r:
            rows+=1
            try:
                pre=root_id(row["pre_root_id_720575940"]); post=root_id(row["post_root_id_720575940"])
                if pre is None or post is None: raise ValueError("missing root")
                p=tuple(float(row[k]) for k in ("pre_x","pre_y","pre_z"))
                q=tuple(float(row[k]) for k in ("post_x","post_y","post_z"))
                s=sums_out[pre]; s[0]+=p[0]; s[1]+=p[1]; s[2]+=p[2]; s[3]+=1
                s=sums_in[post]; s[0]+=q[0]; s[1]+=q[1]; s[2]+=q[2]; s[3]+=1
            except (KeyError,ValueError,TypeError):
                malformed+=1
    out={k:(v[0]/v[3],v[1]/v[3],v[2]/v[3]) for k,v in sums_out.items() if v[3]}
    inc={k:(v[0]/v[3],v[1]/v[3],v[2]/v[3]) for k,v in sums_in.items() if v[3]}
    edges=aggregate_pair_synapses(ep,min_synapses=a.min_synapses)
    nodes={u for u,_ in edges}|{v for _,v in edges}
    both=nodes&out.keys()&inc.keys()
    rng=random.Random(a.seed)
    es=rng.sample(list(edges),min(a.edge_sample,len(edges)))
    ed=[dist(out[u],inc[v]) for u,v in es if u in out and v in inc]
    eset=set(edges); ns=list(nodes); ne=[]; nes=set(); attempts=0; target=min(a.nonedge_sample,len(ns)*(len(ns)-1)-len(edges))
    while len(ne)<target and attempts<max(1000,a.nonedge_sample*50):
        attempts+=1; u,v=rng.sample(ns,2); pair=(u,v)
        if pair in eset or pair in nes:continue
        nes.add(pair);ne.append(pair)
    nd=[dist(out[u],inc[v]) for u,v in ne if u in out and v in inc]
    centroids_path=Path(a.centroids_output)
    centroids_path.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(centroids_path,"wt",newline="") as cf:
        w=csv.writer(cf)
        w.writerow(["root_id","out_x","out_y","out_z","out_synapses","in_x","in_y","in_z","in_synapses"])
        for rid in sorted(nodes):
            o=sums_out[rid]; i=sums_in[rid]
            w.writerow([rid,o[0]/o[3],o[1]/o[3],o[2]/o[3],int(o[3]),i[0]/i[3],i[1]/i[3],i[2]/i[3],int(i[3])])
    result={
      "dataset":"FAFB","version":"v783",
      "purpose":"Gate C0 arbor-aware spatial preflight using Princeton synapse table; no spatial null or scientific conclusion",
      "inputs":{"connections":str(ep),"connections_sha256":sha256(ep),"synapse_table":str(sp),
                "synapse_table_sha256":sha256(sp),"min_synapses":a.min_synapses},
      "synapse_table_schema":{"required_columns":sorted(required),
        "root_id_encoding":"header suffix _720575940 is expanded to canonical 64-bit root ID by prefix concatenation",
        "coordinate_units":"FAFB voxel coordinates","voxel_size_nm":[4,4,40],
        "distance_definition":"source outgoing synapse pre-site centroid to target incoming synapse post-site centroid"},
      "synapse_inventory":{"rows":rows,"malformed_rows":malformed,
        "outgoing_root_ids":len(out),"incoming_root_ids":len(inc)},
      "graph_inventory":{"unique_directed_pairs":len(edges),"graph_nodes":len(nodes),
        "nodes_with_outgoing_centroids":len(nodes&out.keys()),
        "nodes_with_incoming_centroids":len(nodes&inc.keys()),
        "nodes_with_both_centroids":len(both),
        "outgoing_centroid_coverage":len(nodes&out.keys())/len(nodes),
        "incoming_centroid_coverage":len(nodes&inc.keys())/len(nodes),
        "both_centroid_coverage":len(both)/len(nodes)},
      "sampling":{"seed":a.seed,"requested_edge_sample":a.edge_sample,"accepted_edge_sample":len(ed),
        "requested_nonedge_sample":a.nonedge_sample,"candidate_nonedges_generated":len(ne),
        "accepted_nonedge_distance_sample":len(nd),"nonedge_sampling_attempts":attempts},
      "distance_summary":{"observed_edges_nm":quant(ed),"sampled_nonedges_nm":quant(nd)},
      "scientific_conclusion":None,
      "next_gate":"C1 only if both-centroid coverage is sufficient and missingness is characterized; otherwise resolve source coverage before spatial rewiring."
    }
    op=Path(a.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":main()
