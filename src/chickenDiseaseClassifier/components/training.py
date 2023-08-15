import time
import tensorflow as tf
from src.chickenDiseaseClassifier.entity.config_entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config : TrainingConfig):
        self.config  =config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)
    
    def train_valid_generator(self):
# This method will be used to do data_augumentation on the fly.

        datagenerator_kwargs ={"validation_split" :0.2,"rescale" : 1./255}

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator( **datagenerator_kwargs)
        # This is the valid_datagenerator i am creating for validation data
        #  This ImageDataGenerator class in TensorFlow (tf.keras) is a powerful tool for generating augmented batches of 
        # image data during model training. It is primarily used in deep learning tasks, particularly in computer vision
        #  applications, to apply data augmentation techniques to image data.
        # Note : Validation_split = 0.2 will not create any separate folders in my training_data directory.The generator doesn't create separate "validation" and 
        # "training" folders. Instead, it generates batches of data on-the-fly, following the split ratio you've specified.
        # In Python, the double asterisk ** is used to pass a dictionary as a set of keyword arguments to a function or method. 


        dataflow_kwargs = {"target_size" : self.config.params_image_size[:-1], "batch_size" : self.config.params_batch_size,"interpolation": "bilinear"}

        self.validgenerator = valid_datagenerator.flow_from_directory(directory= self.config.training_data, subset="validation", shuffle= "False",**dataflow_kwargs)
        
        # The flow_from_directory() method takes a path of a directory and generates batches of augmented data.
        # subset: This parameter is set to "validation," indicating that you want to generate data for validation purposes.
        #  This assumes that your dataset is structured in a way that you have a separate subdirectory for training data and
        #  another one for validation data.

        train_datagenerator = valid_datagenerator
        # this is the train_datagenerator i am creating for training data. as of now for simplicity i am keeping both the 
        # training and validation datagenerator as same or equal

        self.traingenerator = train_datagenerator.flow_from_directory(directory = self.config.training_data, subset = "training",shuffle = "False",**dataflow_kwargs)
        # This subset= training means data generator will only load the images and labels that are designated as training data.
        
    @staticmethod
    def save_model(path: Path,model: tf.keras.Model):
        model.save(path)

    def train(self,callbacks :list):
        self.model.fit(self.traingenerator,epochs = self.config.params_epochs,batch_size = self.config.params_batch_size,
                       validation_data=self.validgenerator,callbacks = callbacks)
    # I am using the augumented data returned by traingenerator created in above function
    # callbacks: This is a list of callbacks that will be used to monitor the training process and to intervene if necessary.

    # A callback is a set of functions to be applied at given stages of the training procedure.
    # pass a list of callbacks (as the keyword argument callbacks ) to the . fit() method of the Sequential or Model classes.

        self.save_model(self.config.trained_model_path,self.model)