from src.simulator.rss_benchmark import RSSSweepConfig, default_rss_cases, run_rss_case

def test_all_rss_conditions_are_deterministic_and_budgeted():
    config = RSSSweepConfig(modules=9, contexts=3, sequence_length=6, max_active_relations=5)
    for case in default_rss_cases(config):
        first = run_rss_case(case, config)
        second = run_rss_case(case, config)
        assert first == second
        assert all(r.active_relations <= config.max_active_relations for r in first)
        assert all(r.transmitted_bytes == r.active_relations * case.bytes_per_relation for r in first)

def test_dynamic_layers_change_routes_with_context():
    config = RSSSweepConfig(modules=12, contexts=3, sequence_length=6, max_active_relations=4)
    case = next(c for c in default_rss_cases(config) if c.name == "C_dynamic_layered")
    results = run_rss_case(case, config)
    assert len({r.context for r in results}) == 3
    assert sum(r.routing_churn for r in results if r.task == "global") > 0

def test_higher_order_condition_is_explicitly_limited():
    config = RSSSweepConfig(modules=9, contexts=3, sequence_length=3, max_active_relations=5, max_higher_order=1)
    case = next(c for c in default_rss_cases(config) if c.name == "D_dynamic_higher_order")
    results = run_rss_case(case, config)
    assert any(r.higher_order_relations == 1 for r in results if r.task in ("context", "temporal"))
