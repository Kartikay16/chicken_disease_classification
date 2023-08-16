import os 
import urllib.request as request #using this urllib.request to download the dataset from the url
import zipfile 
from chickenDiseaseClassifier import logger
from chickenDiseaseClassifier.utils.common import get_size
from pathlib import Path
from chickenDiseaseClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            file_name,headers = request.urlretrieve(url = self.config.source_url, filename = self.config.local_data_file)
            # The parameters url and filename are used to specify the source URL from which the file should be downloaded 
            # and the local file path where it should be saved, respectively.
            # The function returns a tuple containing the local file path where the file was saved (file_name) and a 
            # dictionary containing the response headers from the server (headers).
            logger.info(f"{file_name} download ! with following info : \n{headers}")
        else:
            logger.info(f"file already exsists of size : {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        # The exist_ok=True argument ensures that if the directory already exists, no error will be raised, 
        # and the function will simply proceed without attempting to create the directory again.

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)