from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{STAGE_NAME} started.")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(f"Error in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Data Validation stage"

try: 
    logger.info(f">>>>> stage{STAGE_NAME} started <<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<")  
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Model Training stage"
try:   
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 