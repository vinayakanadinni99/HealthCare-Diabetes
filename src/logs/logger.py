import logging
import os
from datetime import datetime

# Define log directory (using absolute path)

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(LOG_DIR, exist_ok= True) # Ensure log directory exists

# Define log file paht with Timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE)

# Configure logging to write to the log file
logging.basicConfig(
    filename=  LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.info
)