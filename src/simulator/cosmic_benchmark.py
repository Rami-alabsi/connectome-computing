"""M6-COSMIC matched-resource benchmark primitives.

This module evaluates a narrow engineering question: can a compact global field
carry aggregate information more cheaply than explicit pairwise communication,
and when does it fail on pair-sensitive tasks? It is a synthetic benchmark,
not a physical model of the cosmic web or gravity.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Mapping, Sequence

from .relational_field import FieldConfig, build_global_field

State = tuple[float, ...]
Mode = Literal["field", "sparse", "hybrid"]


@dataclass(frozen=True)
class CosmicCase:
    name: str
    mode: Mode
    field_dim: int
    active_pairs: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class CosmicResult:
    name: str
    mode: Mode
    transmitted_values: int
    transmitted_bytes: int
    global_error: float
    pair_error: float


def _mean(states: Sequence[State]) -> State:
    return tuple(sum(s[i] for s in states) / len(states) for i in range(len(states[0])))


def _pair_target(states: Mapping[int, State], pair: tuple[int, int]) -> State:
    return tuple((states[pair[0]][i] + states[pair[1]][i]) / 2 for i in range(len(next(iter(states.values())))))


def _error(a: Sequence[float], b: Sequence[float]) -> float:
    return sum((float(x) - float(y)) ** 2 for x, y in zip(a, b)) ** 0.5


def run_cosmic_case(
    module_states: Mapping[int, Sequence[float]],
    case: CosmicCase,
    *,
    bytes_per_value: int = 8,
) -> CosmicResult:
    """Run one deterministic aggregate-vs-pair-sensitive information test.

    The receiver is asked to reproduce (1) the global module mean and
    (2) one selected pair aggregate. The field condition sees only its compact
    global field; sparse sees only the states of its explicitly selected pairs;
    hybrid receives both.
    """
    states = {int(k): tuple(float(x) for x in v) for k, v in module_states.items()}
    if not states:
        raise ValueError("module_states must not be empty")
    if any(len(v) != len(next(iter(states.values()))) for v in states.values()):
        raise ValueError("all states must have equal dimension")

    target_global = _mean(list(states.values()))
    if not case.active_pairs:
        raise ValueError("at least one active pair is required")
    pair = case.active_pairs[0]
    if pair[0] not in states or pair[1] not in states:
        raise KeyError("active pair contains unknown module")
    target_pair = _pair_target(states, pair)

    dim = len(target_global)
    values = 0
    if case.mode in ("field", "hybrid"):
        field, report = build_global_field(
            states,
            config=FieldConfig(field_dim=case.field_dim, bytes_per_value=bytes_per_value),
        )
        values += report.transmitted_values
        global_estimate = field if case.field_dim == dim else tuple(
            sum(field) / len(field) for _ in range(dim)
        )
    else:
        global_estimate = target_pair

    if case.mode in ("sparse", "hybrid"):
        # Explicit pair communication transmits both endpoint effective states.
        values += 2 * dim
        pair_estimate = target_pair
    else:
        # A global field contains no module identity; use the field mean as the
        # deterministic pair estimate. This intentionally exposes the limitation.
        pair_estimate = global_estimate[:dim]

    if case.mode == "field":
        # Field compression may lose aggregate coordinates when field_dim < dim.
        global_estimate = tuple(global_estimate[i % len(global_estimate)] for i in range(dim))
    elif case.mode == "hybrid":
        global_estimate = tuple(global_estimate[i % len(global_estimate)] for i in range(dim))

    return CosmicResult(
        name=case.name,
        mode=case.mode,
        transmitted_values=values,
        transmitted_bytes=values * bytes_per_value,
        global_error=_error(global_estimate, target_global),
        pair_error=_error(pair_estimate, target_pair),
    )
