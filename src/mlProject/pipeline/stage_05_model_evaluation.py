from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME = "Model Evaluation stage"  

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.save_results()
    
        except Exception as e:
            logger.exception(f"Error in {STAGE_NAME}: {e}")
            raise e

if __name__ == "__main__": 
    try:
        logger.info(f"{STAGE_NAME} started.")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}: {e}")
        raise e