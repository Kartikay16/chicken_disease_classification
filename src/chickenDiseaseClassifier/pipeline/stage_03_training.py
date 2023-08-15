from src.chickenDiseaseClassifier.config.configuration import ConfigurationManager
from src.chickenDiseaseClassifier.components.training import Training
from src.chickenDiseaseClassifier.components.prepare_callback import PrepareCallback
from chickenDiseaseClassifier import logger


STAGE_NAME = "training"

class Training:
    def __init__(self):
        pass

    def main(self):
        configuration_manager = ConfigurationManager()
        training_config = configuration_manager.get_training_config()
        callback_config = configuration_manager.get_prepare_callback_config()
        callback_obj1 = PrepareCallback(callback_config)
        callbacks = callback_obj1.get_ckpt_tb_callbacks()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callbacks)

if __name__ == "main":
    try:
        logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>")
        training_pipeline = Training()
        training_pipeline.main()
        logger.info(f"stage {STAGE_NAME} completed succesfully <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e