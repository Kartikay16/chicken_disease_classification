from chickenDiseaseClassifier.config.configuration import ConfigurationManager
from chickenDiseaseClassifier.components.model_evaluation import Evaluation
from chickenDiseaseClassifier import logger



STAGE_NAME = "model_evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        configuartion_manager = ConfigurationManager()
        evaluation_config  = configuartion_manager.get_evaluation_config()
        evaluation = Evaluation(evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()


try:
    logger.info(f"stage {STAGE_NAME} started succesfully >>>>>>>>> ")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"stage {STAGE_NAME} completed succesfully <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
        