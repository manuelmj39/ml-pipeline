"""
This Module consists of Data Ingestion Pipeline
"""

import os
import sys

sys.path.append(r"D:\Training\ml-pipeline")

import pandas as pd
import yaml

from src.exception import CustomException
from src.logger import logging

# folder to load config file
CONFIG_PATH = "config/"

# Function to load yaml configuration file
def load_config(config_name: str) -> dict:
    """
    Load configuration file

    This function load the configuration file which
    consists of all the paths, and other miscellaneous
    contents.

    Parameters
    ----------
        config_path: str
            Path to the configuration file

    Returns
    -------
        dict
            Dictionary of configurations
    """
    with open(os.path.join(CONFIG_PATH, config_name)) as config_file:
        config = yaml.safe_load(config_file)

    return config


config = load_config(config_name="main_conf.yaml")


class DataIngestion:
    """
    Class for Data Ingestion Process
    """

    def __init__(self):
        self.raw_bronze_data_path = config["data"]["raw_bronze"]
        self.raw_silver_data_path = config["data"]["raw_silver"]

    def initiate_data_ingestion(self) -> str:
        """ "
        Inititate data Ingestion

        This function initiates the data Ingestion
        process and stores the data in the desired path
        and finally return path location where the data is
        stored

        Raises
        ------
            CustomException: Exception
                Some Custom Exception

        Returns
        -------
            str
                Path where the file got stored
        """
        logging.info("Starting ingestion of data")

        try:
            df = pd.read_csv(self.raw_bronze_data_path)
            logging.info("Loaded the CSV File")

            df.to_csv(self.raw_silver_data_path, index=False, header=True)

            logging.info("Completed Ingestion Process")

            return self.raw_silver_data_path

        except Exception as e:
            logging.info(e)
            raise CustomException(e, sys)


data_ingest_obj = DataIngestion()
data_ingest_obj.initiate_data_ingestion()
