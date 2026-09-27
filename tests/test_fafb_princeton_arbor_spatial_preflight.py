import gzip
from scripts.run_fafb_princeton_arbor_spatial_preflight import root_id

def test_root_id_expansion():
    assert root_id("610757204") == "720575940610757204"
    assert root_id("720575940610757204") == "720575940610757204"

def test_schema_probe_fixture(tmp_path):
    p=tmp_path/"s.csv.gz"
    raw=("pre_x,pre_y,pre_z,ctr_x,ctr_y,ctr_z,post_x,post_y,post_z,size,pre_root_id_720575940,post_root_id_720575940,neuropil\n"
         "1,2,3,2,2,3,4,5,6,1,610757204,620797269,LA_L\n")
    with gzip.open(p,"wt") as f:f.write(raw)
    with gzip.open(p,"rt") as f:
        header=f.readline().strip().split(",")
    assert "pre_x" in header and "post_x" in header
    assert root_id("620797269")=="720575940620797269"
