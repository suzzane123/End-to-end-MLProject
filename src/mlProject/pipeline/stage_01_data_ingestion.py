from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject import logger


STAGE_NAME ="Data Ingestion stage"  

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f"{STAGE_NAME} completed successfully.")
        except Exception as e:
            logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} started.")
        obj = DataIngestionTrainingPipeline()
        obj.main()
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e