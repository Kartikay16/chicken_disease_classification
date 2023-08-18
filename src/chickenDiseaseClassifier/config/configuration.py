from chickenDiseaseClassifier.constants import *
import os
from chickenDiseaseClassifier.utils.common import read_yaml,create_directories
from chickenDiseaseClassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbacksConfig,TrainingConfig,EvaluationConfig

class ConfigurationManager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,params_file_path = PARAM_FILE_PATH):
        
        self.config = read_yaml(config_file_path)
        self.param = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_configuration(self) ->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(root_dir = config.root_dir,
                                                    source_url=config.source_url,
                                                    local_data_file = config.local_data_file, 
                                                    unzip_dir = config.unzip_dir)
        return data_ingestion_config

    def get_prepare_base_model_configuration(self) -> PrepareBaseModelConfig :
        config = self.config.prepare_base_model

        prepare_base_model_config = PrepareBaseModelConfig(
                                                root_dir = Path(config.root_dir),
                                                base_model_path = Path(config.base_model_path),
                                                updated_base_model_path= Path(config.updated_base_model_path),
                                                params_image_size = self.param.IMAGE_SIZE,
                                                params_learning_rate = self.param.LEARNING_RATE,
                                                params_include_top = self.param.INCLUDE_TOP,
                                                params_weights = self.param.WEIGHTS,
                                                params_classes = self.param.CLASSES
                                                )
        return prepare_base_model_config
    
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        # This is a function from the os.path module that returns the directory name component of a given file path. 
        # It takes the file path as an argument and extracts the directory part, excluding the file name
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])

        prepare_callback_config = PrepareCallbacksConfig(root_dir = config.root_dir, 
                                                         tensorboard_root_log_dir = config.tensorboard_root_log_dir,
                                                         checkpoint_model_filepath = config.checkpoint_model_filepath
                                                        )
        return prepare_callback_config

    def get_training_config(self) -> TrainingConfig:
        trn = self.config.training
        param = self.param
        pbm = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir , "Chicken-fecal-images")
        create_directories([trn.root_dir])

        training_config = TrainingConfig(   root_dir = Path(trn.root_dir),
                                            trained_model_path= Path(trn.trained_model_path),
                                            updated_base_model_path = Path(self.config.prepare_base_model.updated_base_model_path),
                                            training_data = Path(training_data),
                                            params_epochs= param.EPOCHS,
                                            params_batch_size= param.BATCH_SIZE,
                                            params_is_augmentation  =param.AUGMENTATION,
                                            params_image_size= param.IMAGE_SIZE
                                            )
        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:

        evaluation_config = EvaluationConfig(
                                        path_of_model = self.config.training.trained_model_path,
                                        training_data = os.path.join(self.config.data_ingestion.unzip_dir , "Chicken-fecal-images"),
                                        all_params = self.param,
                                        params_image_size= self.param.IMAGE_SIZE,
                                        params_batch_size = self.param.BATCH_SIZE
        )
        return evaluation_config