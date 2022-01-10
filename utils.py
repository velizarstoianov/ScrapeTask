import logging
import os
from datetime import date

def log_message(message, level_of_log):
    filename = date.today().strftime("%d-%m-%Y")
    filename +=".log"
    filepath = os.path.join(os.getcwd(),"log/"+filename)
    if(not os.path.exists(filepath)):
        open(filepath,"x")
    logging.basicConfig(filename=filepath, level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    if(level_of_log=="error"):
        logger.error(message)
        return
    if(level_of_log=="warning"):
        logger.warning(message)
        return
    if(level_of_log=="info"):
        logger.info(message)
        return