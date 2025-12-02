from src.ds_project.logger import logging
from src.ds_project.exception import CustomException
from src.ds_project.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.ds_project.components.data_transformation import DataTransformation, DataTransformationConfig
from src.ds_project.components.model_trainer import ModelTrainer, ModelTrainerConfig
import sys


if __name__ == "__main__":
    logging.info("Application started executing")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        # model training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    
        
    except Exception as e:
        logging.info("this is custom exception(app.py)")
        raise CustomException(e, sys)
