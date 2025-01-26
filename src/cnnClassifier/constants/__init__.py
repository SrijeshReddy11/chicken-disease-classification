from pathlib import Path

print("Loading constants module...")  # Debug print

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

__all__ = [
    "CONFIG_FILE_PATH",
    "PARAMS_FILE_PATH"
]