"""Sparse modular directed graph generation for large node counts.

Unlike the original Bernoulli generator, this implementation samples candidate
edges in expected O(E) time rather than scanning all N^2 source-target pairs.
It is a scalable baseline, not a biological generator.
"""
from __future__ import annotations

import random
from .modular import GeneratorConfig


def generate_sparse_modular_directed(
    config: GeneratorConfig,
    *,
    target_edges: int | None = None,
    seed: int = 0,
) -> set[tuple[int, int]]:
    """Generate a sparse modular graph by direct candidate sampling."""
    if config.nodes < 2:
        raise ValueError("nodes must be at least 2")
    if config.modules < 1 or config.modules > config.nodes:
        raise ValueError("modules must be between 1 and nodes")
    if not 0 <= config.p_intra <= 1 or not 0 <= config.p_inter <= 1:
        raise ValueError("edge probabilities must be in [0, 1]")
    if not 0 <= config.hub_fraction <= 1 or config.hub_multiplier < 1:
        raise ValueError("invalid hub configuration")

    max_edges = config.nodes * (config.nodes - 1) if not config.self_loops else config.nodes ** 2
    if target_edges is None:
        module_fraction = 1.0 / config.modules
        expected_density = config.p_intra * module_fraction + config.p_inter * (1.0 - module_fraction)
        target_edges = round(expected_density * max_edges)
    if target_edges < 0 or target_edges > max_edges:
        raise ValueError("target_edges is outside the possible edge range")
    if target_edges == 0:
        return set()

    rng = random.Random(seed)
    module_of = [min(config.modules - 1, node * config.modules // config.nodes) for node in range(config.nodes)]
    module_ranges = []
    for module in range(config.modules):
        start = module * config.nodes // config.modules
        end = (module + 1) * config.nodes // config.modules
        module_ranges.append((start, end))

    hub_count = max(1, int(config.nodes * config.hub_fraction))
    hubs = rng.sample(range(config.nodes), hub_count)
    hub_set = set(hubs)

    edges: set[tuple[int, int]] = set()
    intra_weight = config.p_intra
    inter_weight = config.p_inter
    module_weight = intra_weight / max(intra_weight + inter_weight, 1e-12)
    max_attempts = max(1000, target_edges * 50)
    attempts = 0

    while len(edges) < target_edges and attempts < max_attempts:
        attempts += 1
        source = rng.randrange(config.nodes)
        source_module = module_of[source]

        if rng.random() < module_weight:
            start, end = module_ranges[source_module]
        else:
            other_module = rng.randrange(config.modules - 1) if config.modules > 1 else source_module
            if config.modules > 1 and other_module >= source_module:
                other_module += 1
            start, end = module_ranges[other_module]

        # Hub-biased target sampling. This is intentionally explicit so that the
        # synthetic baseline can be compared with a no-hub ablation.
        hub_bias = config.hub_multiplier / (config.hub_multiplier + max(end - start, 1))
        if rng.random() < hub_bias:
            target = rng.choice(hubs)
            if not (start <= target < end):
                target = rng.randrange(start, end)
        else:
            target = rng.randrange(start, end)

        if target == source and not config.self_loops:
            continue
        edges.add((source, target))

    if len(edges) < target_edges:
        raise RuntimeError(
            f"could only generate {len(edges)} of {target_edges} requested edges "
            f"after {attempts} attempts"
        )
    return edges
