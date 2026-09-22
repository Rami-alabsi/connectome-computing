"""Configurable modular directed graph generator."""
from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable


@dataclass(frozen=True)
class GeneratorConfig:
    nodes: int = 1000
    modules: int = 10
    p_intra: float = 0.03
    p_inter: float = 0.003
    hub_fraction: float = 0.02
    hub_multiplier: float = 4.0
    self_loops: bool = False


def generate_modular_directed(config: GeneratorConfig, seed: int = 0) -> set[tuple[int, int]]:
    """Generate a directed modular graph from explicit structural probabilities.

    This is a baseline generator, not a claim that biological connectomes follow
    this exact stochastic process.
    """
    if config.nodes < 1:
        raise ValueError("nodes must be positive")
    if config.modules < 1 or config.modules > config.nodes:
        raise ValueError("modules must be between 1 and nodes")
    if not 0 <= config.p_intra <= 1 or not 0 <= config.p_inter <= 1:
        raise ValueError("edge probabilities must be in [0, 1]")
    if not 0 <= config.hub_fraction <= 1 or config.hub_multiplier < 1:
        raise ValueError("invalid hub configuration")

    rng = random.Random(seed)
    module_of = {i: min(config.modules - 1, i * config.modules // config.nodes) for i in range(config.nodes)}
    hubs = set(rng.sample(range(config.nodes), max(1, int(config.nodes * config.hub_fraction))))

    edges: set[tuple[int, int]] = set()
    for source in range(config.nodes):
        for target in range(config.nodes):
            if source == target and not config.self_loops:
                continue
            same_module = module_of[source] == module_of[target]
            probability = config.p_intra if same_module else config.p_inter
            if source in hubs or target in hubs:
                probability = min(1.0, probability * config.hub_multiplier)
            if rng.random() < probability:
                edges.add((source, target))
    return edges


def module_sizes(config: GeneratorConfig) -> list[int]:
    sizes = [0] * config.modules
    for node in range(config.nodes):
        sizes[min(config.modules - 1, node * config.modules // config.nodes)] += 1
    return sizes
