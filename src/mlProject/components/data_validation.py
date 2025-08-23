import os
from mlProject import logger

import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        logger.info(f"DataValidation initialized with config: {self.config}")
    
    def validate_column(self) -> bool:
        try: 
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"Validation status: {validation_status}\n")
            return validation_status
        except Exception as e:
            raise e