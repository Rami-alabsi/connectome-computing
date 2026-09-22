from src.generator.modular import GeneratorConfig, generate_modular_directed, module_sizes


def test_generator_is_reproducible():
    config = GeneratorConfig(nodes=50, modules=5, p_intra=0.2, p_inter=0.02)
    assert generate_modular_directed(config, seed=7) == generate_modular_directed(config, seed=7)


def test_generator_has_expected_node_range_and_no_self_loops():
    config = GeneratorConfig(nodes=30, modules=3, p_intra=0.2, p_inter=0.02)
    edges = generate_modular_directed(config, seed=3)
    assert all(0 <= u < 30 and 0 <= v < 30 for u, v in edges)
    assert all(u != v for u, v in edges)


def test_module_sizes_sum_to_nodes():
    config = GeneratorConfig(nodes=101, modules=7)
    assert sum(module_sizes(config)) == config.nodes
