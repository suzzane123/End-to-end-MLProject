from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation

from mlProject import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_column()
    
if __name__ == "__main__":
    try:
        logger.info(">>>>> stage_02_data_validation started <<<<<")
        data_validation_training_pipeline = DataValidationTrainingPipeline()
        data_validation_training_pipeline.main()
        logger.info(">>>>> stage_02_data_validation completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e