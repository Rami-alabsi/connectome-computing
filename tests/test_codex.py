from src.ingestion.codex import resource_url

def test_resource_url_contains_dataset_and_product():
    url = resource_url("connections_princeton", "fafb")
    assert "connections_princeton" in url
    assert "dataset=fafb" in url
