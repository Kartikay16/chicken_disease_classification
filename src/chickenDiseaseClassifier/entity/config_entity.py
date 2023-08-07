# I can create my own custom return type using entity

from dataclasses import dataclass
# Data classes simplify the creation of classes that primarily 
# store data, as they automatically generate special methods like __init__, __repr__, and more.
from pathlib import Path


# The frozen=True argument makes the class immutable, 
# meaning that once an instance of this class is created, its attributes cannot be modified
@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir:Path
    source_url:Path
    local_data_file:Path
    unzip_dir:Path


@dataclass(frozen = True)
class PrepareBaseModelConfig:
    root_dir :Path
    base_model_path : Path
    updated_base_model_path : Path
    params_image_size :list
    params_learning_rate :float
    params_include_top : bool
    params_weights: str 
    params_classes : int


@dataclass(frozen =True)
class PrepareCallbacksConfig:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_filepath:Path