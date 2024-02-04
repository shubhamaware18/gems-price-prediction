import pandas as pd
from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self, config):
        self.ingestion_config = config

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Started')

        try:
            data = pd.read_csv('data_files/raw.csv')
            logging.info('Reading a DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("I have saved the raw dataset in the artifacts folder")

            logging.info("I have PERFORMED TRAIN TEST SPLIT")

            train_data, test_data = train_test_split(data, test_size=0.25)

            logging.info('Train Test split completed')

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("data ingestion part completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        # except logic
        except Exception as e:
            # print(e)
            logging.error(str(e))
            raise customexception(e, sys)

if __name__ == "__main__":
    config = DataIngestionConfig()
    obj = DataIngestion(config)
    obj.initiate_data_ingestion()
