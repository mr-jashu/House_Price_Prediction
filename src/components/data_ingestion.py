import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Generating synthetic data for House Prices
            np.random.seed(42)
            n_samples = 1000
            
            # Features
            MedInc = np.random.normal(5, 2, n_samples) # Median Income
            HouseAge = np.random.normal(30, 10, n_samples) # House Age
            AveRooms = np.random.normal(6, 2, n_samples) # Avg Rooms
            AveBedrms = np.random.normal(1, 0.5, n_samples) # Avg Bedrooms
            Population = np.random.normal(1500, 500, n_samples)
            AveOccup = np.random.normal(3, 1, n_samples) # Avg Occupancy
            Latitude = np.random.normal(35, 2, n_samples)
            Longitude = np.random.normal(-120, 2, n_samples)
            
            # Target: Price (synthetic relationship)
            Price = (MedInc * 2) + (HouseAge * 0.1) + (AveRooms * 0.5) + np.random.normal(0, 1, n_samples)
            Price = Price * 50000 # Scaling to realistic price range
            
            df = pd.DataFrame({
                'MedInc': MedInc, 'HouseAge': HouseAge, 'AveRooms': AveRooms,
                'AveBedrms': AveBedrms, 'Population': Population, 'AveOccup': AveOccup,
                'Latitude': Latitude, 'Longitude': Longitude, 'Target': Price
            })
            
            logging.info('Synthetic dataset created')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)