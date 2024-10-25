import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# shows a log file in a specific naming convention
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# logs created are w.r.t. present working directory
os.makedirs(logs_path, exist_ok = True)
    # even if there's files in the folder, keep appending files into this

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # asctime is ascending time, then line number, then name
    # ie: [ 2024-10-25 18:22:22,969 ] 24 root - INFO - Logging started
)

# this creates file logs based on the given formats

if __name__=="__main__":
    logging.info("Logging started")