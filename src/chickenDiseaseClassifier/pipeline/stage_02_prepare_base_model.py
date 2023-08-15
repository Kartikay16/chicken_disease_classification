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

# The __name__ variable in Python is a special variable that holds the name of the current module or 
# script.
#  When a Python script is executed, Python sets the __name__ variable based on how the script is being
#  used. There are two primary scenarios:

# Script Execution:
# When a Python script is directly executed as the main program, the __name__ variable is set to '__main__'.

# Module Import:
# When a Python script is imported as a module into another script, the __name__ variable is set to the name 
# of the module (i.e., the name of the script without the .py extension).



if __name__ == '__main__':
    try:
        logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>")
        prepare_base_model_training_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_training_pipeline.main()
        logger.info(f"stage {STAGE_NAME} completed succesfully <<<<<<<<")
    except Exception as  e:
        logger.exception(e)
        raise e