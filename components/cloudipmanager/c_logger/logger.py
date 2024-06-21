import logging
from cloudipmanager.c_skeleton.default_global_variables import global_variables # type: ignore
import socket

class Logger:
    
    def __init__(self, levelname, logger_name, extras={}):
        self.levelname = levelname
        self.logger_name = logger_name
        self.extras = extras

    def get_logger(self) -> logging.LoggerAdapter:
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
        default_extras: dict = {
            "hostname" : socket.gethostname(),
            "ipaddress" : socket.gethostbyname(socket.gethostname()),
        }
        final_extras = {**default_extras, **self.extras}
        log_seperator = ":"
        formatting_string = "%(asctime)s " + log_seperator + " %(module)s " + log_seperator + " %(levelname)s " + log_seperator + " %(message)s " + log_seperator
        for extra in final_extras:
            formatting_string = formatting_string + " %(" + extra + ")s " + log_seperator
        formatting_string=formatting_string[:-1:]
        formatter = logging.Formatter(formatting_string)
        file_handler=logging.FileHandler(global_variables.LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        log_adapter = logging.LoggerAdapter(logger, extra=final_extras)
        return log_adapter