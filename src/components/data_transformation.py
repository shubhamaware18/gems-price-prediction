import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys

from dataclasses import dataclass
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass


    # method for data ingestion
    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)
        

