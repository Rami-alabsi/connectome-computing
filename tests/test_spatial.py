from src.generator.spatial import distance_decay_probability, mean_edge_length

def test_distance_decay():
    assert distance_decay_probability(0,length_scale=1)==1
    assert distance_decay_probability(1,length_scale=1)<1

def test_mean_edge_length():
    positions={0:(0.0,0.0),1:(1.0,0.0),2:(0.0,2.0)}
    assert mean_edge_length({(0,1),(1,2)},positions)>0
