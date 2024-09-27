import logging
import os
import sys
from datetime import datetime

# Set up log file with current timestamp
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logging_format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"

# Define the log directory inside 'src/logs'
log_dir = 'logs'
log_filepath = os.path.join(log_dir,"running_logs.log")   

# Create the 'logs' directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Full path to the log file
# logs_path = os.path.join(log_dir, LOG_FILE)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
    
)

logger = logging.getLogger("us-visa-approval-logger")
