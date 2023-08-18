from chickenDiseaseClassifier import logger
from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier.components.training import Training
from chickenDiseaseClassifier.components.prepare_callback import PrepareCallback




STAGE_NAME = "training"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # logger.info(f"Entering this {STAGE_NAME} stage ")
        configuration_manager = ConfigurationManager()
        training_config = configuration_manager.get_training_config()
        # logger.info("Got training config object")
        callback_config = configuration_manager.get_prepare_callback_config()
        # logger.info("Got callback config object")
        callback_obj1 = PrepareCallback(callback_config)
        callbacks = callback_obj1.get_ckpt_tb_callbacks()
        training = Training(training_config)
        # logger.info("Getting base model")
        training.get_base_model()
        # logger.info("Getting data Generator")
        training.train_valid_generator()
        # logger.info("Training")
        training.train(callbacks)

# # logger.info("Trying to enter conditional statement")
# if __name__ == "main":
#     try:
#         logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>")
#         training_pipeline = TrainingPipeline()
#         training_pipeline.main()
#         logger.info(f"stage {STAGE_NAME} completed succesfully <<<<<<<<")
#     except Exception as e:
#         logger.exception(e)
#         raise e


STAGE_NAME = "training"
try:
      logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>")
      training_pipeline = TrainingPipeline()
      training_pipeline.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e
