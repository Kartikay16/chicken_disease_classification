import tensorflow as tf
from src.chickenDiseaseClassifier.entity.config_entity import EvaluationConfig
from pathlib import Path
from chickenDiseaseClassifier.utils.common import save_json



class Evaluation:
    def __init__(self,config :EvaluationConfig):
            self.config = config
    

    def get_valid_generator(self):

        datagenerator_kwargs ={"validation_split" :0.2,"rescale" : 1./255}

        data_generator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        

        dataflow_kwargs = {"target_size" :self.config.params_image_size[:-1],"batch_size":self.config.params_batch_size,"interpolation" : "bilinear"}
        self.valid_generator = data_generator.flow_from_directory(directory = self.config.training_data, subset = "validation",shuffle = False,**dataflow_kwargs)

    @staticmethod
    def load_model(path : Path) -> tf.keras.Model:
         return tf.keras.models.load_model(path)
    

    def evaluation(self):
         self.model = self.load_model(self.config.path_of_model)
         self.get_valid_generator()
         self.score = self.model.evaluate(self.valid_generator)

    def save_score(self):
         scores = {"loss" : self.score[0] , "accuracy" : self.score[1]}
         save_json(path = Path("scores.json"),data = scores)
