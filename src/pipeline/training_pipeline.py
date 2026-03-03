import sys
import os

try:
    from src.components.data_ingestion import DataIngestion
    from src.components.data_transformation import DataTransformation
    from src.components.model_trainer import ModelTrainer
    from src.logger import logging
    from src.exception import CustomException
except ModuleNotFoundError:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from src.components.data_ingestion import DataIngestion
    from src.components.data_transformation import DataTransformation
    from src.components.model_trainer import ModelTrainer
    from src.logger import logging
    from src.exception import CustomException

if __name__ == "__main__":
    try:
        logging.info("Training Pipeline Started")
        
        # 1. Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # 2. Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        # 3. Model Training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        
        print(f"Training Completed. Best Model R2 Score: {r2_score}")
        logging.info(f"Training Pipeline Completed. R2 Score: {r2_score}")
        
    except Exception as e:
        logging.info("Exception occured in Training Pipeline")
        raise CustomException(e, sys)