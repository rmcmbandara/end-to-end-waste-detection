import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_directory = os.path.join(from_root(), 'log')
log_path = os.path.join(log_directory, LOG_FILE)

# Create the 'log' directory if it doesn't exist
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
