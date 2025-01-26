import os
import sys
import logging
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

logging_str = "[%(asctime)s] %(levelname)s %(name)s - %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

__all__ = [
    "CONFIG_FILE_PATH",
    "PARAMS_FILE_PATH"
]