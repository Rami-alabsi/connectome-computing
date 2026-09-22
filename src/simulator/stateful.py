"""Minimal stateful simulator for the M6 resource-constrained architecture.

The simulator deliberately separates:
1. local node dynamics,
2. module-level effective-state formation,
3. state-dependent route selection,
4. bounded cross-module communication,
5. redistribution of received module messages.

It is a classical engineering testbed. It is not a biological neuron model.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import tanh
from typing import Mapping, Sequence

from .effective_state import InterfaceConfig, build_effective_messages
from .routing import RoutingConfig, RoutingReport, select_state_dependent_routes

State = tuple[float, ...]
Edge = tuple[int, int]


@dataclass(frozen=True)
class SimulatorConfig:
    """Resource and dynamics parameters for one simulator step."""

    interface_dim: int
    max_active_pairs: int
    local_decay: float = 0.9
    coupling: float = 0.2
    bytes_per_value: int = 8

    def __post_init__(self) -> None:
        if self.interface_dim < 1:
            raise ValueError("interface_dim must be positive")
        if self.max_active_pairs < 1:
            raise ValueError("max_active_pairs must be positive")
        if not 0.0 <= self.local_decay <= 1.0:
            raise ValueError("local_decay must be in [0, 1]")
        if self.coupling < 0.0:
            raise ValueError("coupling must be non-negative")
        if self.bytes_per_value < 1:
            raise ValueError("bytes_per_value must be positive")


@dataclass(frozen=True)
class StepReport:
    """Accounting and routing information for one simulation step."""

    routing: RoutingReport
    candidate_cross_edges: int
    active_module_pairs: int
    transmitted_values: int
    transmitted_bytes: int


def _validate_states(node_states: Mapping[int, Sequence[float]]) -> dict[int, State]:
    if not node_states:
        raise ValueError("node_states must not be empty")
    states = {node: tuple(float(x) for x in state) for node, state in node_states.items()}
    width = len(next(iter(states.values())))
    if width < 1:
        raise ValueError("node states must be non-empty")
    if any(len(state) != width for state in states.values()):
        raise ValueError("all node states must have equal dimension")
    return states


def _module_means(
    states: Mapping[int, State],
    node_to_module: Mapping[int, int],
) -> dict[int, State]:
    members: dict[int, list[State]] = {}
    for node, state in states.items():
        if node not in node_to_module:
            raise KeyError("every node must have a module assignment")
        members.setdefault(node_to_module[node], []).append(state)

    return {
        module: tuple(sum(state[i] for state in values) / len(values) for i in range(len(values[0])))
        for module, values in members.items()
    }


def _filter_edges(
    edges: Sequence[Edge],
    node_to_module: Mapping[int, int],
    active_pairs: set[tuple[int, int]],
) -> tuple[Edge, ...]:
    return tuple(
        (u, v)
        for u, v in edges
        if u in node_to_module
        and v in node_to_module
        and node_to_module[u] != node_to_module[v]
        and (node_to_module[u], node_to_module[v]) in active_pairs
    )


def step(
    node_states: Mapping[int, Sequence[float]],
    node_edges: Sequence[Edge],
    node_to_module: Mapping[int, int],
    candidate_pairs: Sequence[tuple[int, int]],
    *,
    config: SimulatorConfig,
) -> tuple[dict[int, State], StepReport]:
    """Advance one deterministic local-plus-interface simulation step.

    Local state is updated with a bounded recurrent decay term. Cross-module
    communication is formed from compact module messages after state-dependent
    route selection. Each received message is then broadcast to nodes in the
    destination module as a deliberately simple baseline.
    """
    states = _validate_states(node_states)
    module_states = _module_means(states, node_to_module)

    routing_config = RoutingConfig(
        max_active_pairs=config.max_active_pairs,
        bytes_per_value=config.bytes_per_value,
        values_per_message=config.interface_dim,
    )
    active_pairs, routing_report = select_state_dependent_routes(
        module_states,
        candidate_pairs,
        config=routing_config,
    )

    active_set = set(active_pairs)
    active_edges = _filter_edges(node_edges, node_to_module, active_set)
    interface_config = InterfaceConfig(
        interface_dim=config.interface_dim,
        max_module_pairs=config.max_active_pairs,
        bytes_per_value=config.bytes_per_value,
    )
    messages, communication = build_effective_messages(
        states,
        active_edges,
        node_to_module,
        config=interface_config,
    )

    incoming: dict[int, list[State]] = {module: [] for module in module_states}
    for (source, target), message in messages.items():
        del source
        incoming.setdefault(target, []).append(message)

    next_states: dict[int, State] = {}
    for node, state in states.items():
        module = node_to_module[node]
        received = incoming.get(module, [])
        updated = []
        for index, value in enumerate(state):
            drive = 0.0
            for message in received:
                if index < len(message):
                    drive += message[index]
            updated.append(tanh(config.local_decay * value + config.coupling * drive))
        next_states[node] = tuple(updated)

    report = StepReport(
        routing=routing_report,
        candidate_cross_edges=communication.candidate_cross_edges,
        active_module_pairs=communication.active_module_pairs,
        transmitted_values=communication.transmitted_values,
        transmitted_bytes=communication.transmitted_bytes,
    )
    return next_states, report
