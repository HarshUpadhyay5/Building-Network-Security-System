from Networksecurity.Components.data_ingestion import DataIngestion
from Networksecurity.Exception.exception import NetworkSecurityException
from Networksecurity.Logging.logger import logging
from Networksecurity.Entity.config_entity import Data_Ingestion_Config
from Networksecurity.Entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        data_ingestion = DataIngestion(Data_Ingestion_Config(TrainingPipelineConfig()))
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)