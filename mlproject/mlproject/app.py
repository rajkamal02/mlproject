from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig, DataTransformation
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Initialize Data Ingestion
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(data_ingestion_config)
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Initialize Data Transformation
        data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        raise CustomException(e, sys)
