"""Classical field-mediated coordination primitive for M6-COSMIC.

A compact global field is formed from module-level effective states and can be
broadcast without exposing node-level states. The field is an engineering
abstraction inspired by multiscale field-mediated coordination; it is not a
physical model of gravity, quantum fields, or spacetime.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Mapping, Sequence

State = tuple[float, ...]
ModuleId = int


@dataclass(frozen=True)
class FieldConfig:
    """Resource limits for one global latent-field payload."""

    field_dim: int
    bytes_per_value: int = 8

    def __post_init__(self) -> None:
        if self.field_dim < 1:
            raise ValueError("field_dim must be positive")
        if self.bytes_per_value < 1:
            raise ValueError("bytes_per_value must be positive")


@dataclass(frozen=True)
class FieldReport:
    """Communication accounting for one field construction/broadcast."""

    source_modules: int
    field_values: int
    transmitted_values: int
    transmitted_bytes: int


def build_global_field(
    module_states: Mapping[ModuleId, Sequence[float]],
    *,
    config: FieldConfig,
) -> tuple[State, FieldReport]:
    """Compress module states into one deterministic global field vector.

    The baseline uses permutation-invariant mean pooling followed by contiguous
    coordinate grouping. It deliberately has no learned parameters.
    """
    if not module_states:
        raise ValueError("module_states must not be empty")
    values = [tuple(float(x) for x in state) for _, state in sorted(module_states.items())]
    width = len(values[0])
    if width < 1:
        raise ValueError("module states must be non-empty")
    if any(len(state) != width for state in values):
        raise ValueError("all module states must have equal dimension")
    if config.field_dim > width:
        raise ValueError("field_dim must not exceed module-state dimension")

    pooled = tuple(
        sum(state[i] for state in values) / len(values)
        for i in range(width)
    )
    if config.field_dim == width:
        field = pooled
    else:
        boundaries = [ceil(i * width / config.field_dim) for i in range(config.field_dim + 1)]
        field = tuple(
            sum(pooled[i] for i in range(boundaries[j], boundaries[j + 1]))
            / (boundaries[j + 1] - boundaries[j])
            for j in range(config.field_dim)
        )

    report = FieldReport(
        source_modules=len(values),
        field_values=len(field),
        transmitted_values=len(field),
        transmitted_bytes=len(field) * config.bytes_per_value,
    )
    return field, report


def broadcast_field(
    field: Sequence[float],
    module_ids: Sequence[ModuleId],
) -> dict[ModuleId, State]:
    """Expose the same compact field state to each destination module."""
    value = tuple(float(x) for x in field)
    if not value:
        raise ValueError("field must be non-empty")
    return {module: value for module in sorted(set(module_ids))}
