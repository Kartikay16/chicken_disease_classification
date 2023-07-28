from src.chickenDiseaseClassifier.components.data_ingestion import DataIngestion
from src.chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            configuration_manager = ConfigurationManager()
            data_ingestion_configuration  = configuration_manager.get_data_ingestion_configuration()
            data_ingestion = DataIngestion(config = data_ingestion_configuration)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} started succesfully <<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"stage {STAGE_NAME} completed <<<<<<<<<")
    except Exception as  e:
        logger.exception(e)
        raise e
