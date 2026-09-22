"""Calibrate a synthetic generator from an observed structural profile."""
from __future__ import annotations
from dataclasses import replace
from .modular import GeneratorConfig
from .profile import StructuralProfile


def calibrate_config(profile: StructuralProfile, *, nodes: int | None = None, modules: int = 10, p_intra: float | None = None, p_inter_ratio: float = 0.1, hub_fraction: float = 0.02, hub_multiplier: float = 4.0) -> GeneratorConfig:
    """Create a first-order generator config from observed graph statistics.

    This is a calibration baseline, not a fitted biological model. The resulting
    graph must be measured again and compared with the source profile.
    """
    target_nodes = nodes if nodes is not None else profile.nodes
    if target_nodes < 1:
        raise ValueError("nodes must be positive")
    if p_intra is None:
        p_inter = min(1.0, profile.density * p_inter_ratio)
        module_fraction = 1.0 / max(modules, 1)
        p_intra = min(1.0, max(profile.density, (profile.density - p_inter * (1 - module_fraction)) / module_fraction))
    else:
        p_inter = min(1.0, p_intra * p_inter_ratio)
    return GeneratorConfig(
        nodes=target_nodes,
        modules=modules,
        p_intra=p_intra,
        p_inter=p_inter,
        hub_fraction=hub_fraction,
        hub_multiplier=hub_multiplier,
    )
