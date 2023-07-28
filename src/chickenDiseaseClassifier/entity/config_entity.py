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