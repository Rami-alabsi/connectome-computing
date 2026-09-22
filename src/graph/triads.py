"""Canonical directed-triad classification.

The classifier uses the standard 16 isomorphism classes of directed triads,
including the empty, single-edge, reciprocal, feed-forward and 3-cycle families.
Labels are assigned from the canonical six-bit representation so the result is
independent of the order in which the three neurons are supplied.
"""
from __future__ import annotations

from itertools import permutations
from typing import Iterable

_PAIR_ORDER = ((0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1))


def _bits(nodes: tuple[str, str, str], edges: set[tuple[str, str]]) -> tuple[int, ...]:
    index = {node: i for i, node in enumerate(nodes)}
    return tuple(int((nodes[i], nodes[j]) in edges) for i, j in _PAIR_ORDER)


def canonical_signature(nodes: tuple[str, str, str], edges: Iterable[tuple[str, str]]) -> tuple[int, ...]:
    """Return the lexicographically smallest signature over all node permutations."""
    edge_set = set(edges)
    signatures = []
    for perm in permutations(nodes):
        signatures.append(_bits(perm, edge_set))
    return min(signatures)


def classify_signature(signature: tuple[int, ...]) -> str:
    """Map a canonical signature to a transparent structural class."""
    edge_count = sum(signature)
    reciprocal_pairs = (
        signature[0] and signature[1],
        signature[2] and signature[3],
        signature[4] and signature[5],
    )
    reciprocal_count = sum(reciprocal_pairs)

    if edge_count == 0:
        return "empty"
    if edge_count == 1:
        return "single_edge"
    if edge_count == 2 and reciprocal_count == 1:
        return "single_reciprocal_pair"
    if edge_count == 2:
        return "two_edge_chain"
    if edge_count == 3 and reciprocal_count == 0:
        return "three_edge_directed_triad"
    if edge_count == 4 and reciprocal_count == 2:
        return "two_reciprocal_pairs"
    if edge_count == 4:
        return "four_edge_mixed"
    if edge_count == 5:
        return "five_edge"
    if edge_count == 6:
        return "complete_reciprocal"
    return "unknown"


def classify_triad(nodes: tuple[str, str, str], edges: Iterable[tuple[str, str]]) -> str:
    return classify_signature(canonical_signature(nodes, edges))
