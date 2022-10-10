import logging
from dotenv import load_dotenv
import os

load_dotenv()

# FUNCTION TO CREATE THE LOGGING DIREECTORY IF IT DOES NOT EXIST
level = os.environ.get("LOGGING_LEVEL")


def create_log():
    logging.basicConfig(filename='./logs/log.log', level=level,
                        format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    if not os.path.exists('./logs'):
        print("log directory does not exist")
        print("creating logfile directory: ./logs")
        os.makedirs('./logs')
