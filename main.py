import sys
from security.components.data_ingestion import DataIngestion
from security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from security.exception.exception import NetworkSecurityException
from security.logging.logger import lg

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestconfig)
        lg.info("Initiate the data Ingestion")

        dataingestartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)