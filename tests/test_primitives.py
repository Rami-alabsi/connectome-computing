from pathlib import Path

from src.architecture.primitives import (
    ArchitecturePrimitive,
    DEFAULT_PRIMITIVES,
    load_primitives,
    save_primitives,
)


def test_default_primitives_are_hypotheses():
    assert len(DEFAULT_PRIMITIVES) >= 5
    assert all(item.status == "hypothesis" for item in DEFAULT_PRIMITIVES)


def test_primitive_round_trip(tmp_path: Path):
    item = ArchitecturePrimitive(
        "TEST",
        "Test",
        "biology",
        "structure",
        "mechanism",
        "property",
        "falsification",
    )
    path = tmp_path / "primitives.json"
    save_primitives([item], path)
    assert load_primitives(path) == [item]
