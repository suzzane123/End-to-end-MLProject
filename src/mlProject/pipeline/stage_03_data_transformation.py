from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as file:
                status = file.read().split(" ")[-1].strip()
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception(f"Data validation failed. Status: {status}")
        except Exception as e:
            print(e)