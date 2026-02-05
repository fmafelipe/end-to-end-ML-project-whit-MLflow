import os 
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_data(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            list_status = []

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    list_status.append("False")
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status col {col}: {validation_status} \n")
                
                else:
                    validation_status = True
                    list_status.append("True")
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status col {col}: {validation_status} \n")

            if "False" in list_status:
                validation_status = False

            else:
                validation_status = True
            
            return validation_status

        except Exception as e:
            raise e
    