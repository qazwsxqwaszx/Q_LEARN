import logging
from src.utils.logger import setup_logger

def test_setup_logger_creates_file_and_sets_level(tmp_path):
    config_file = tmp_path / "config.yaml"
    log_file = tmp_path / "logs/test.log"
    config_file.write_text(f"""
logging:
  level: DEBUG
  file: {log_file}
  format: "%(levelname)s:%(message)s"
""")
    # Reset existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger = setup_logger(config_path=str(config_file))
    logger.debug("hello")

    assert log_file.exists()
    content = log_file.read_text()
    assert "hello" in content
    assert logger.getEffectiveLevel() == logging.DEBUG
