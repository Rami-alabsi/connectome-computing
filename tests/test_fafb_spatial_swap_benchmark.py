from scripts.run_fafb_spatial_swap_benchmark import dbin, degree_maps
def test_distance_bins():
    assert dbin(0)==0
    assert dbin(50_000)==2
    assert dbin(9_999_999)==8
def test_degree_maps():
    i,o=degree_maps([("a","b"),("c","b"),("a","d")])
    assert i["b"]==2 and o["a"]==2
