import os
import sys

sys.path.append(r"D:\Training\ml-pipeline")

import pickle

import yaml

from src.exception import CustomException
from src.logger import logging

# folder to load config file
CONFIG_PATH = r"config/"

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


# Function to save pickle objects
def save_object(file_path: str, obj: object) -> None:
    """
    Function to Save a pickle object

    Parameters
    ----------
        file_path:
            Path where object needs to be saved

        obj:
            Obnject to be saved

    Raises
    ------
        CustomException: Exception
            Some Custom Exception

    Returns
    -------
        None
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.info(CustomException(e, sys))
