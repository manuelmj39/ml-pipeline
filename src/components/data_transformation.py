"""
This Module consists of Data Transformation Pipeline
"""
import sys

sys.path.append(r"D:\Training\ml-pipeline")

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import load_config, save_object

# Loading Configuration Settings
config = load_config(config_name="main_conf.yaml")


class DataTransformation:
    """
    Class for Data Transformation processes
    """

    def get_train_test_split(self) -> pd.DataFrame:
        """
        Train Test Splitting

        Function to split the raw dataset into
        train and test datasets.

        Returns
        -------
        pd.Dataframe
            Train Dataset and Test Dataset
        """
        raw_data_path = config["data"]["raw_silver"]

        raw_data = pd.read_csv(raw_data_path)
        train_set, test_set = train_test_split(
            raw_data, test_size=0.2
        )

        return train_set, test_set

    def get_data_transformer_object(self):
        """
        Data Transformation Function

        Function to convert the categorical columns
        into numerical columns and applying standardizations
        method on the dataframe

        Raises
        ------
            CustomException: Exception
                Some Custom Exception

        Returns
        ------
            ColumnTransformer
                Column Transfromer Object
        """
        try:
            numerical_columns = ["writing_score", "reading_score"]

            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    (
                        "imputer",
                        SimpleImputer(strategy="most_frequent"),
                    ),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False)),
                ]
            )

            logging.info(
                f"Categorical columns: {categorical_columns}"
            )
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                [
                    (
                        "num_pipeline",
                        numerical_pipeline,
                        numerical_columns,
                    ),
                    (
                        "cat_pipelines",
                        categorical_pipeline,
                        categorical_columns,
                    ),
                ]
            )

            return preprocessor

        except Exception as e:
            logging.info(CustomException(e, sys))

    def initiate_data_transformation(self):
        """
        Initiate Data Transformation Function

        Function to start the Data Transformation
        process and returns the transformed datasets

        Raises
        ------
            CustomException: Exception
                Some Custom Exception

        Returns
        -------
            np.array
                Numpy array for Transormed Train and test set.

            str
                Path where the Column Transofmer object is saved
        """
        train_data, test_data = self.get_train_test_split()

        try:
            logging.info("Reading train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"

            input_feature_train_df = train_data.drop(
                columns=[target_column_name], axis=1
            )
            target_feature_train_df = train_data[target_column_name]

            input_feature_test_df = test_data.drop(
                columns=[target_column_name], axis=1
            )
            target_feature_test_df = test_data[target_column_name]

            logging.info(
                "Applying preprocessing object on training \
                dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df
            )
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df
            )

            train_arr = np.c_[
                input_feature_train_arr,
                np.array(target_feature_train_df),
            ]
            test_arr = np.c_[
                input_feature_test_arr,
                np.array(target_feature_test_df),
            ]

            save_object(
                file_path=config["preprocessor"][
                    "column_preprocessor_pipe"
                ],
                obj=preprocessing_obj,
            )

            logging.info("Saved preprocessing object.")

            return (
                train_arr,
                test_arr,
                config["preprocessor"]["column_preprocessor_pipe"],
            )
        except Exception as e:
            logging.info(CustomException(e, sys))


data_transformer = DataTransformation()
data_transformer.initiate_data_transformation()
