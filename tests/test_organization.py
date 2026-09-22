from src.graph.organization import (
    hierarchy_crossing_fraction,
    hierarchy_distance,
    long_range_fraction,
    module_edge_fractions,
    participation_coefficients,
)


def test_participation_coefficients():
    edges = [(1, 2), (1, 3), (1, 4), (2, 3)]
    labels = {1: "a", 2: "a", 3: "b", 4: "b"}
    values = participation_coefficients(edges, labels)
    assert round(values[1], 6) == round(4 / 9, 6)


def test_module_edge_fractions():
    edges = [(1, 2), (1, 3), (3, 4)]
    labels = {1: "a", 2: "a", 3: "b", 4: "b"}
    result = module_edge_fractions(edges, labels)
    assert result == {"within_fraction": 2 / 3, "between_fraction": 1 / 3}


def test_hierarchy_crossing_fraction():
    edges = [(1, 2), (1, 3), (3, 4)]
    hierarchy = {
        1: ("A", "A1"),
        2: ("A", "A2"),
        3: ("B", "B1"),
        4: ("B", "B2"),
    }
    assert hierarchy_crossing_fraction(edges, hierarchy, level=0) == 1 / 3
    assert hierarchy_distance(hierarchy, 1, 2) == 1
    assert hierarchy_distance(hierarchy, 1, 3) == 0


def test_long_range_fraction():
    edges = [(1, 2), (1, 3), (2, 3)]
    positions = {1: (0.0, 0.0), 2: (1.0, 0.0), 3: (3.0, 0.0)}
    assert long_range_fraction(edges, positions, threshold=2.0) == 2 / 3
