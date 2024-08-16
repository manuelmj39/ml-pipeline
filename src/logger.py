import os
import logging
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_PATH, exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE_NAME)

#Basic Config Setup
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(pathname)s : %(lineno)d - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
    )

logging.info("Logging has started")