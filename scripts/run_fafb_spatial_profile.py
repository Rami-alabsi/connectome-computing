#!/usr/bin/env python3
"""Profile FAFB v783 connection rows by synapse neuropil and pair multiplicity.

This is a descriptive spatial/mesoscale inventory. The connection-table
"neuropil" field identifies the synapse location, not a complete pre/post
neuron compartment label. It is therefore not itself a neuropil-constrained
null model.
"""
from __future__ import annotations
import argparse, csv, json
from collections import Counter, defaultdict
from pathlib import Path
from src.graph.connections import _open_csv, _pick, SOURCE_CANDIDATES, TARGET_CANDIDATES, WEIGHT_CANDIDATES

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="data/raw/fafb_v783/connections_princeton.csv.gz")
    ap.add_argument("--output",default="artifacts/fafb-v783/spatial-profile.json")
    args=ap.parse_args()
    rows=0
    synapses=0
    regions=Counter()
    region_synapses=Counter()
    pair_regions=defaultdict(set)
    pair_rows=Counter()
    with _open_csv(Path(args.input)) as fh:
        reader=csv.DictReader(fh)
        if not reader.fieldnames: raise ValueError("missing CSV header")
        s=_pick(reader.fieldnames,SOURCE_CANDIDATES)
        t=_pick(reader.fieldnames,TARGET_CANDIDATES)
        w=next((c for c in WEIGHT_CANDIDATES if c in reader.fieldnames),None)
        region_col="neuropil" if "neuropil" in reader.fieldnames else None
        if region_col is None: raise ValueError("expected neuropil column")
        for row in reader:
            u,v=row[s],row[t]
            region=row[region_col]
            rows += 1
            regions[region] += 1
            pair_regions[(u,v)].add(region)
            pair_rows[(u,v)] += 1
            if w:
                try:
                    x=int(float(row[w]))
                except (TypeError,ValueError):
                    x=0
                synapses += x
                region_synapses[region] += x
    multiplicity=Counter(pair_rows.values())
    multi_pairs=sum(n for k,n in multiplicity.items() if k>1)
    result={
      "dataset":"FAFB","version":"v783",
      "raw_rows":rows,
      "unique_directed_pairs":len(pair_rows),
      "neuropil_count":len(regions),
      "total_synapses":synapses,
      "multi_region_unique_pairs":multi_pairs,
      "multi_region_pair_fraction":multi_pairs/len(pair_rows) if pair_rows else 0.0,
      "pair_row_multiplicity_histogram":{str(k):v for k,v in sorted(multiplicity.items())},
      "neuropil_rows":dict(regions),
      "neuropil_synapses":dict(region_synapses),
      "definition":"neuropil is the synapse-location field in the public connection table; it is not a complete neuron-level pre/post neuropil assignment.",
      "null_model_status":"descriptive inventory only; no spatially constrained null is claimed here."
    }
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
