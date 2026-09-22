from src.generator.modular import GeneratorConfig
from src.generator.sparse import generate_sparse_modular_directed


def test_sparse_generator_reproducible():
    config = GeneratorConfig(nodes=500, modules=10, p_intra=0.02, p_inter=0.002)
    a = generate_sparse_modular_directed(config, target_edges=2000, seed=11)
    b = generate_sparse_modular_directed(config, target_edges=2000, seed=11)
    assert a == b


def test_sparse_generator_hits_requested_edge_count_without_self_loops():
    config = GeneratorConfig(nodes=200, modules=5, p_intra=0.02, p_inter=0.002)
    edges = generate_sparse_modular_directed(config, target_edges=500, seed=3)
    assert len(edges) == 500
    assert all(u != v for u, v in edges)
