from src.generator.profile import StructuralProfile
from src.generator.validation import compare_profiles


def test_profile_comparison_reports_absolute_and_relative_error():
    observed = StructuralProfile(100, 200, 200 / (100 * 99), 2.0, 2.0, 0.1)
    synthetic = StructuralProfile(100, 220, 220 / (100 * 99), 2.2, 2.2, 0.12)
    result = compare_profiles(observed, synthetic)
    assert result.absolute_error["directed_edges"] == 20.0
    assert result.relative_error["directed_edges"] == 0.1
    assert abs(result.absolute_error["reciprocal_edge_fraction"] - 0.02) < 1e-12
