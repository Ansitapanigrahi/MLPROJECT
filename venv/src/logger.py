import logging 
import os
from datetime import datetime

# Define log folder path
LOG_FOLDER = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_FOLDER, exist_ok=True)

# Define log file name with timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log file path
LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)




