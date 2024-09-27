import logging
import os
from datetime import datetime

# Set up log file with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory inside 'src/logs'
log_dir = os.path.join('src', 'logs')

# Create the 'logs' directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Full path to the log file
logs_path = os.path.join(log_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging.info("Logging setup complete.")
