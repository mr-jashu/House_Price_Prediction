import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def predict(self, features):
        try:
            # FIXED PATH LOGIC: Get the absolute path to the root directory
            # This file is in src/pipeline, so we go up 2 levels to reach root
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.dirname(os.path.dirname(current_dir))
            
            model_path = os.path.join(root_dir, "artifacts", "model.pkl")
            preprocessor_path = os.path.join(root_dir, "artifacts", "preprocessor.pkl")
            
            print(f"Loading model from: {model_path}")
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
            
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude):
        self.MedInc = MedInc
        self.HouseAge = HouseAge
        self.AveRooms = AveRooms
        self.AveBedrms = AveBedrms
        self.Population = Population
        self.AveOccup = AveOccup
        self.Latitude = Latitude
        self.Longitude = Longitude

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "MedInc": [self.MedInc], "HouseAge": [self.HouseAge],
                "AveRooms": [self.AveRooms], "AveBedrms": [self.AveBedrms],
                "Population": [self.Population], "AveOccup": [self.AveOccup],
                "Latitude": [self.Latitude], "Longitude": [self.Longitude]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)