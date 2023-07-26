import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'chickenDiseaseClassifier'

list_of_files = [

    ".github/workflows/.gitkeep",
    # we are keeping this gitkeep file in this workflows folder because otherwise
# workflow folder will be emplty and git wont reflect empty folders.
    f"src/{project_name}/__init__.py",
    # This __init__.py file is needed to make this project of mine as a python proejct and whatever 
    # i create here can be used by proper imports in some other python project as well.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml" ,
    # since we will be implimenting mLOps tools so we nee this yaml files
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    #  To perform notebook experiments i am creating this research folder
]

for file_path in list_of_files:
    file_path = Path(file_path)
#  I am passing all my file paths through Path because here i have used forward slash and in windows operating system
# we use backward slashes so modifying the path to fit to windows standards

# to seprate fodler name from file name
    file_dir,file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir,exist_ok = True)
        # parameter exist_ok = True means the filedirectory i am passing is already present.Otherwise it will again create the file directory
        logging.info("creating directory; {file_dir} for the {file_name}")

    # Now for file if a file doesnot exsist or size of file is 0
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        # So now create the file 
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating an empty file: {file_path}")
    else:
        logging.info(f"{file_path} already exists")
       