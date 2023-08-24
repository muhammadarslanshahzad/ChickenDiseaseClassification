import sys
sys.path.append('/mnt/e/cv_mlops/src')  # Add the path to the 'src' folder

from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline


###
# Data Ingestion Stage Pipeline
####
STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n xxxxxxxxxxxx===================================================================================================================xxxxxxxxxxxxxx')
except Exception as e:
    logger.exception(e)
    raise e



###
#  Preparing Base Model Pipeline 
###
STAGE_NAME = 'Prepare Base Model'
try:
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n xxxxxxxxxxxx===================================================================================================================xxxxxxxxxxxxxx')
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e