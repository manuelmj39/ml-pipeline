import os
import sys
import yaml

import pandas as pd

from src.logger import logging
from src.exception import CustomException

# folder to load config file
CONFIG_PATH = "config/"

# Function to load yaml configuration file
def load_config(config_name):
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config

config = load_config("main_conf.yaml")

class DataIngestion:
    def __init__(self):
        self.raw_bronze_data_path = config['data']['raw_bronze']
        self.raw_silver_data_path = config['data']['raw_silver']

    def initiate_data_ingestion(self):
        logging.info("Starting ingestion of data")

        try:
            df = pd.read_csv(self.raw_bronze_data_path)
            logging.info("Loaded the CSV File")

            df.to_csv(self.raw_silver_data_path, 
                      index=False, header=True)
            
            logging.info("Completed Ingestion Process")

            return (self.raw_silver_data_path)

        except Exception as e:
            logging.info(e)
            raise CustomException(e, sys)
        
data_ingest_obj = DataIngestion()
data_ingest_obj.initiate_data_ingestion()