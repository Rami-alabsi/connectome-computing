from src.generator.calibration import calibrate_config
from src.generator.profile import StructuralProfile


def test_calibration_targets_profile_scale_and_density():
    profile = StructuralProfile(100, 990, 990/(100*99), 9.9, 9.9, 0.1)
    config = calibrate_config(profile, modules=5, p_inter_ratio=0.1)
    assert config.nodes == 100
    assert 0 < config.p_inter <= config.p_intra <= 1


def test_calibration_can_scale_nodes():
    profile = StructuralProfile(100, 990, 990/(100*99), 9.9, 9.9, 0.1)
    config = calibrate_config(profile, nodes=1000, modules=20)
    assert config.nodes == 1000
