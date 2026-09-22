import random
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CapacityHierarchy:
    """Static hierarchy produced by bounded module capacity.

    The model is intentionally generic: capacity is an architectural constraint,
    not an atomic or biological parameter.
    """
    node_to_module: tuple[int, ...]
    node_to_path: tuple[tuple[int, ...], ...]
    module_nodes: tuple[tuple[int, ...], ...]
    parent_modules: tuple[tuple[int, ...], ...]


def build_capacity_hierarchy(
    n: int,
    *,
    module_capacity: int,
    hierarchy_depth: int = 2,
    modules_per_parent: int = 4,
) -> CapacityHierarchy:
    if n < 1:
        raise ValueError("n must be positive")
    if module_capacity < 1 or hierarchy_depth < 1 or modules_per_parent < 1:
        raise ValueError("capacity, depth, and modules_per_parent must be positive")

    # Saturation rule: fill a module to capacity, then create the next peer.
    node_to_module = tuple(i // module_capacity for i in range(n))
    module_count = (n + module_capacity - 1) // module_capacity

    node_to_path = []
    for i, module in enumerate(node_to_module):
        path = [0] * hierarchy_depth
        value = module
        for level in range(hierarchy_depth - 1, -1, -1):
            path[level] = value % modules_per_parent
            value //= modules_per_parent
        node_to_path.append(tuple(path))

    module_nodes = [[] for _ in range(module_count)]
    for node, module in enumerate(node_to_module):
        module_nodes[module].append(node)

    parent_groups = {}
    for module, path in enumerate(node_to_path[::module_capacity] if False else []):
        parent_groups.setdefault(path[:-1], []).append(module)

    # Parent identity is derived from the module index, not node labels.
    parent_groups = {}
    for module in range(module_count):
        value = module
        parent = value // modules_per_parent
        parent_groups.setdefault(parent, []).append(module)

    return CapacityHierarchy(
        node_to_module=node_to_module,
        node_to_path=tuple(node_to_path),
        module_nodes=tuple(tuple(x) for x in module_nodes),
        parent_modules=tuple(tuple(x) for _, x in sorted(parent_groups.items())),
    )


def capacity_hierarchy_graph(
    n: int,
    target_edges: int,
    *,
    module_capacity: int,
    hierarchy_depth: int = 2,
    modules_per_parent: int = 4,
    internal_weight: float = 1.0,
    sibling_weight: float = 0.25,
    external_weight: float = 0.05,
    interface_budget: int = 2,
    seed: int = 0,
) -> tuple[set[tuple[int, int]], CapacityHierarchy]:
    """Generate a directed graph under bounded local capacity.

    Saturation creates new peer modules. External communication is additionally
    limited by a per-module interface budget (counted as incident external
    neighbours). The generator targets an exact edge count when feasible.
    """
    if target_edges < 0 or target_edges > n * (n - 1):
        raise ValueError("target_edges outside simple directed graph capacity")
    if interface_budget < 0:
        raise ValueError("interface_budget must be non-negative")

    structure = build_capacity_hierarchy(
        n,
        module_capacity=module_capacity,
        hierarchy_depth=hierarchy_depth,
        modules_per_parent=modules_per_parent,
    )
    rng = random.Random(seed)
    module_of = structure.node_to_module
    parent_of = {
        m: m // modules_per_parent for m in range(len(structure.module_nodes))
    }

    candidates = []
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            mu, mv = module_of[u], module_of[v]
            if mu == mv:
                weight = internal_weight
                relation = "internal"
            elif parent_of[mu] == parent_of[mv]:
                weight = sibling_weight
                relation = "sibling"
            else:
                weight = external_weight
                relation = "external"
            candidates.append((u, v, max(0.0, weight), relation))

    rng.shuffle(candidates)
    rng.shuffle(candidates)

    chosen = set()
    external_interfaces = [set() for _ in structure.module_nodes]

    def allowed(u: int, v: int, relation: str) -> bool:
        if relation == "internal":
            return True
        mu, mv = module_of[u], module_of[v]
        return (
            len(external_interfaces[mu] | {mv}) <= interface_budget
            and len(external_interfaces[mv] | {mu}) <= interface_budget
        )

    weighted = sorted(
        candidates,
        key=lambda x: (-x[2], rng.random()),
    )
    for u, v, weight, relation in weighted:
        if weight <= 0 or len(chosen) >= target_edges:
            break
        if not allowed(u, v, relation):
            continue
        if relation != "internal":
            mu, mv = module_of[u], module_of[v]
            external_interfaces[mu].add(mv)
            external_interfaces[mv].add(mu)
        chosen.add((u, v))

    # Complete the requested edge budget without violating the interface rule
    # whenever possible. This keeps the generator useful as a matched-budget
    # control; if the interface budget itself makes the target infeasible, the
    # largest feasible graph is returned.
    if len(chosen) < target_edges:
        remaining = [(u, v, r) for u, v, _, r in candidates if (u, v) not in chosen]
        rng.shuffle(remaining)
        for u, v, relation in remaining:
            if len(chosen) >= target_edges:
                break
            if not allowed(u, v, relation):
                continue
            if relation != "internal":
                mu, mv = module_of[u], module_of[v]
                external_interfaces[mu].add(mv)
                external_interfaces[mv].add(mu)
            chosen.add((u, v))

    return chosen, structure
