# Step - Creating/Updating Components

import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.layers import Flatten,Dense
from keras.models import Sequential
from pathlib import Path
from chickenDiseaseClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:

    def __init__(self, config :PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = VGG16(include_top = self.config.params_include_top, input_shape = self.config.params_image_size, weights = self.config.params_weights)
        self.save_model(path = self.config.base_model_path, model = self.model)
    
    @staticmethod
    def save_model(path,model):
        model.save(path)

    
    @staticmethod
    def prepare_full_base_model(model,learning_rate,classes):

        for layer in model.layers:
            layer.trainable = False
        
        model = Sequential(model)
        model.add(Flatten())
        dense_layer1 = Dense(units = classes, activation = "softmax")
        model.add(dense_layer1)

        model.compile( optimizer= tf.keras.optimizers.SGD(learning_rate=learning_rate),loss = tf.keras.losses.CategoricalCrossentropy(),metrics = ['accuracy'])
        model.summary()
        return model 
    
    def update_full_model(self):
        self.full_model = self.prepare_full_base_model(model = self.model,learning_rate = self.config.params_learning_rate, classes = self.config.params_classes)
        self.save_model(self.config.updated_base_model_path,self.full_model)
   