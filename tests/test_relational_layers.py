from src.simulator.relational_layers import (
    LayeredRoute,
    LayeredRoutingConfig,
    RelationalLayer,
    select_dynamic_layered_routes,
)


def test_context_can_shift_active_layer_under_same_budget():
    layers = {
        "local": RelationalLayer("local", priority=1.0),
        "global": RelationalLayer("global", priority=1.0),
    }
    candidates = (
        LayeredRoute(0, 1, "local", 1.0),
        LayeredRoute(2, 3, "global", 1.0),
    )
    local, _ = select_dynamic_layered_routes(
        candidates, layers=layers, context_priority={"local": 2.0, "global": 1.0},
        config=LayeredRoutingConfig(1),
    )
    global_, _ = select_dynamic_layered_routes(
        candidates, layers=layers, context_priority={"local": 1.0, "global": 2.0},
        config=LayeredRoutingConfig(1),
    )
    assert local[0].layer == "local"
    assert global_[0].layer == "global"


def test_overlapping_layers_share_same_nodes_but_have_separate_routes():
    layers = {
        "family": RelationalLayer("family", priority=1.0, max_active_pairs=1),
        "work": RelationalLayer("work", priority=1.0, max_active_pairs=1),
    }
    candidates = (
        LayeredRoute(0, 1, "family", 2.0),
        LayeredRoute(0, 2, "work", 2.0),
        LayeredRoute(0, 3, "family", 1.0),
    )
    selected, report = select_dynamic_layered_routes(
        candidates, layers=layers, config=LayeredRoutingConfig(2)
    )
    assert len(selected) == 2
    assert report.active_by_layer == (("family", 1), ("work", 1))


def test_global_budget_and_bytes_are_explicit():
    layers = {"local": RelationalLayer("local")}
    candidates = tuple(LayeredRoute(i, i + 1, "local", float(i)) for i in range(5))
    selected, report = select_dynamic_layered_routes(
        candidates, layers=layers, config=LayeredRoutingConfig(2, bytes_per_route=16)
    )
    assert len(selected) == 2
    assert report.transmitted_bytes == 32
