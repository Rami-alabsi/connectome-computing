from src.generator.hierarchy import hierarchical_directed_graph, hierarchical_labels

def test_hierarchy_labels_are_nested():
    labels=hierarchical_labels(16,levels=(2,2))
    assert len(labels)==16
    assert all(len(x)==2 for x in labels)

def test_hierarchy_generator_hits_exact_target():
    edges=hierarchical_directed_graph(20,80,levels=(2,5),seed=7)
    assert len(edges)==80
    assert all(u!=v for u,v in edges)
