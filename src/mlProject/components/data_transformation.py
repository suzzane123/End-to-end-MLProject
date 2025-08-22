import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        logger.info(f"DataTransformation initialized with config: {self.config}")
    
    ##Note you can different data transformation techniques such as scaler , pca 
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        logger.info("Starting train-test split")
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        train.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info("Splitted data into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)