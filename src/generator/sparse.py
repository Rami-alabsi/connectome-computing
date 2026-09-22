"""Sparse modular directed graph generation for large node counts."""
from __future__ import annotations
import random
from .modular import GeneratorConfig

def generate_sparse_modular_directed(
    config: GeneratorConfig,
    *,
    target_edges: int | None = None,
    seed: int = 0,
) -> set[tuple[int, int]]:
    """Generate exactly target_edges without an O(N^2) candidate scan."""
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
    module_ranges = [
        (m * config.nodes // config.modules, (m + 1) * config.nodes // config.modules)
        for m in range(config.modules)
    ]
    hubs = rng.sample(range(config.nodes), max(1, int(config.nodes * config.hub_fraction)))
    hub_set = set(hubs)

    # Sample source/target pairs directly. We deliberately keep the proposal
    # simple and deterministic; the measured graph, not the proposal, is the
    # scientific object that is validated.
    intra_share = config.p_intra / max(config.p_intra + config.p_inter, 1e-12)
    edges: set[tuple[int, int]] = set()
    attempts = 0
    max_attempts = max(1000, target_edges * 100)

    while len(edges) < target_edges and attempts < max_attempts:
        attempts += 1
        source = rng.randrange(config.nodes)
        sm = module_of[source]
        if config.modules > 1 and rng.random() >= intra_share:
            other = rng.randrange(config.modules - 1)
            if other >= sm:
                other += 1
            start, end = module_ranges[other]
        else:
            start, end = module_ranges[sm]

        # Mixture of uniform and hub-biased target selection.
        if hub_set and rng.random() < (config.hub_multiplier - 1) / max(config.hub_multiplier, 1):
            target = rng.choice(hubs)
            if not (start <= target < end) and rng.random() < 0.75:
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
