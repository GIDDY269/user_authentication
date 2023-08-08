import pandas as pd
import numpy as np
import urllib.request
from dataclasses import dataclass
import os
import sys
sys.path.append(r'C:\Users\user\user_authenication')
from src.logger import logging
from src.exception import CustomException
import subprocess
import shutil



@dataclass
class data_ingestion_config:
    data_filepath = os.path.join('artifacts' , 'matches')




class data_ingestion:

    def __init__(self) :
        self.data_filepath = data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info('initiated data ingestion')
        
        try:
            if os.path.exists(self.data_filepath.data_filepath) and os.path.getsize(self.data_filepath.data_filepath) > 0:
                print('Data already download')
                logging.info('Data already download')
            
            else :

                os.makedirs('artifacts',exist_ok=True)
                
                logging.info('downloading data')

                repo_url = 'https://github.com/smerdov/eSports_Sensors_Dataset.git'

                temporal_path = r'C:/Users/user/Downloads/temp_repo'
                source_path = r'C:/Users/user/Downloads/temp_repo/matches'
                destination_path = 'artifacts'


                # download the data repository into a temporary folder
                subprocess.run(
                    [
                        'git','clone', repo_url , temporal_path
                    ],check=True
                )

                logging.info('moving data to artifacts folder')

                # moving folder 
                shutil.move(source_path,destination_path)


                logging.info('deleting temporary folder')
                command = f'rmdir /s /q "{temporal_path}"'
                os.system(command)

                logging.info(f'downloded data completed')

        except Exception as e:
            raise CustomException(e , sys)
        

if __name__ == '__main__' :
    obj = data_ingestion()
    obj.initiate_data_ingestion()