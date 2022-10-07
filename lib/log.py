import logging
import os

# FUNCTION TO CREATE THE LOGGING DIREECTORY IF IT DOES NOT EXIST


def create_log():
    logging.basicConfig(filename='./logs/log.log', level=logging.DEBUG,
                        format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    if not os.path.exists('./logs'):
        print("log directory does not exist")
        print("creating logfile directory: ./logs")
        os.makedirs('./logs')
