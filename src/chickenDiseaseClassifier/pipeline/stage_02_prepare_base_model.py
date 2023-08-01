from chickenDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier import logger


STAGE_NAME = "prepare_base_model"

class PrepareBaseModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        configuration_manager = ConfigurationManager()
        prepare_base_model_config = configuration_manager.get_prepare_base_model_configuration()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_full_model()


if __name__ == '__main__':
    try:
        logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>")
        prepare_base_model_training_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_training_pipeline.main()
        logger.info(f"stage {STAGE_NAME} completed succesfully <<<<<<<<")
    except Exception as  e:
        logger.exception(e)
        raise e