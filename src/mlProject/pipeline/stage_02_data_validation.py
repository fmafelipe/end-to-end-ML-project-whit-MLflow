from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

# 7. Update the pipeline

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        status = data_validation.validate_all_data()
        if status == False:
            logger.info("Data validation failed")
            raise Exception(f"Data validation failed, check file {data_validation_config.STATUS_FILE}")



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e