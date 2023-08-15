import time
import tensorflow as tf
from src.chickenDiseaseClassifier.entity.config_entity import PrepareCallbacksConfig
import os

class PrepareCallback:
    def __init__(self,config : PrepareCallbacksConfig):
        self.config  =config
    
    @property
    #  This is a Python decorator that marks the method as a property.
    #  It allows the method to be accessed like an attribute without the need for explicit function call parentheses.
    def create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir, f"tensorboard_logs_at_{timestamp}")
        

        return tf.keras.callbacks.TensorBoard(log_dir  = tb_running_log_dir)
        # The code snippet tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir) creates a TensorBoard callback 
        # instance in TensorFlow Keras. 
        # This callback is used to log training and evaluation metrics during the model training process at the specified position. 

    @property
    def create_checkpoint_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(self.config.checkpoint_model_filepath,save_best_only=True)
    # It is used to save the model's weights during the training process

    def get_ckpt_tb_callbacks(self):
        return [self.create_tb_callbacks , self.create_checkpoint_callbacks]    