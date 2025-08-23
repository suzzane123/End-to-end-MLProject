from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_path = model_trainer.train_model()
            logger.info(f"Model trained and saved at: {model_path}")
        except Exception as e:
            logger.exception("Error during model training")
            raise e
        
        
if __name__ == "__main__":
    try:
        logger.info("Model Training Pipeline started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info("Model Training Pipeline completed successfully")
    except Exception as e:
        logger.exception(f"Error in Model Training Pipeline: {e}")
        raise e