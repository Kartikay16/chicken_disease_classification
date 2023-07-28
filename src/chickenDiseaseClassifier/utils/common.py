# utils is a file containing functions that will be frequently needed in code. So functions to be repeatedly
# used can be just imported from src.utils 

import os
from box.exceptions import BoxValueError
import yaml
from chickenDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded sucesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories :list , verbose =True):
    # The verbose option specifies that you want to display detailed
    #  processing information on your screen.
    for path in path_to_directories:
        os.makedirs(path,exist_ok= True)
        if verbose:
            logger.info(f"Create directory at : {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent = 4)

@ensure_annotations
def load_json(path : Path) ->ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path} ")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data : Any,path :Path):
    joblib.dump(value = data, file_name = Path)
    # joblib is like pickle but has some advantages over pickle.
    logger.info("Binary file saved at:{path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path)-> str:
     """get size in KB"""
     size_in_kb = round(os.path.getsize(path)/1024)
     return f"~ {size_in_kb} KB"

# Encoding prevents the data from getting corrupted 
# when it is transferred or processed through a text-only system.base 64 is used
# for encoding and decoding of the data

def decode_image(img_string,fileName):
    img_data = base64.b64decode(img_string)
    with open(fileName,'wb') as f:
        f.write(img_data)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())


# use of conifg box is if there is a dictionary and i want to have value associated with thay key using 
# this syntax dictionary_name.key_name instead of conventional method like dictionary_name['key_name'] then 
# make this dictionary as configBox type dictionary 
# like this : ConfigBox(pass_the_dictionary_here)

# use of ensure annotations 
# if i use ensure_annotations it will help me identify hidden errors.
# e.g make a function def get_product(x:int,y:int) ->int: return x*y
# now in this function if i pass x as 2 and y as "4"(a string) i will get an output as 44. Now since i am getting wrong
# output so i will not be able to figure out whats going wrong in my code in large codes.
# But if i use @ensure_annotations above my function declaration an the i pass x = 2 and y="4" it will give me an error 
# saying y should be of type int.












