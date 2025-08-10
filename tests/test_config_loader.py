import pytest
from src.utils.config_loader import load_config

def test_load_config_valid(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("key: value\n")
    result = load_config(str(config_path))
    assert result == {"key": "value"}


def test_load_config_missing_file():
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent.yaml")
