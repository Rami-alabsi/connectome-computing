import json
from pathlib import Path
from scripts.run_fafb_spatial_profile import main

def test_spatial_profile_fixture(tmp_path, monkeypatch):
    src=tmp_path/"x.csv"
    src.write_text(
        "pre_root_id,post_root_id,neuropil,syn_count,nt_type\n"
        "1,2,A,3,ach\n"
        "1,2,B,4,ach\n"
        "2,3,A,2,gaba\n"
        "3,2,A,1,gaba\n"
    )
    out=tmp_path/"o.json"
    monkeypatch.setattr("sys.argv",["x","--input",str(src),"--output",str(out)])
    main()
    d=json.loads(out.read_text())
    assert d["raw_rows"]==4
    assert d["unique_directed_pairs"]==3
    assert d["neuropil_count"]==2
    assert d["multi_region_unique_pairs"]==1
    assert d["total_synapses"]==10
