import logging
from cloudipmanager.c_skeleton.default_global_variables import global_variables # type: ignore

class logs:
    def __init__(self, levelname, logger_name):
        self.levelname = levelname
        self.logger_name = logger_name
    
    def logger(self):
        logger = logging.getLogger(self.logger_name)
        if self.levelname == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif self.levelname == "INFO":
            logger.setLevel(logging.INFO)
        elif self.levelname == "WARNING":
            logger.setLevel(logging.WARNING)
        elif self.levelname == "ERROR":
            logger.setLevel(logging.ERROR)
        elif self.levelname == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler=logging.FileHandler(global_variables.LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger