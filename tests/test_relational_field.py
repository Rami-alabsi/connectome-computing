from src.simulator.relational_field import FieldConfig, broadcast_field, build_global_field


def test_global_field_is_deterministic_and_compact():
    modules = {
        2: (1.0, 2.0, 3.0, 4.0),
        0: (3.0, 4.0, 5.0, 6.0),
    }
    field, report = build_global_field(modules, config=FieldConfig(field_dim=2))

    assert field == (2.0, 3.0)
    assert report.source_modules == 2
    assert report.field_values == 2
    assert report.transmitted_values == 2
    assert report.transmitted_bytes == 16


def test_field_broadcast_does_not_expose_node_states():
    field = (0.5, -0.25)
    exposed = broadcast_field(field, [2, 0, 2])

    assert exposed == {0: (0.5, -0.25), 2: (0.5, -0.25)}
    assert all(len(state) == 2 for state in exposed.values())


def test_field_dimension_is_validated():
    try:
        build_global_field({0: (1.0,), 1: (2.0,)}, config=FieldConfig(field_dim=2))
    except ValueError:
        pass
    else:
        raise AssertionError("field dimension validation did not trigger")
