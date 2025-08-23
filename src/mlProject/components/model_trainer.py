import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib


class ModelTrainer:
    def __init__(self, config):
        self.config = config
        logger.info(f"ModelTrainer initialized with config: {self.config}")

    def train_model(self):
        try:
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            train_x = train_data.drop(columns=[self.config.target_column], axis=1)
            test_x = test_data.drop(columns=[self.config.target_column], axis=1)
            train_y = train_data[self.config.target_column]
            test_y = test_data[self.config.target_column]

            model = ElasticNet(
                alpha=self.config.alpha,
                l1_ratio=self.config.l1_ratio,
                random_state=42
            )
            model.fit(train_x, train_y)

            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(model, model_path)
            logger.info(f"Model trained and saved at {model_path}")

            return model_path
        except Exception as e:
            logger.exception("Error during model training")
            raise e