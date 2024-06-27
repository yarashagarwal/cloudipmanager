from cloudipmanager.c_skeleton.default_global_variables import global_variables # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore

logs_error = Logger("Error", "logger_db_connection")
logger_error = logs_error.get_logger()

class DbConnection:
    def __init__(self, mode):
        self.file_name=global_variables.DB_FILE
        self.mode = mode
        
    def open_connection(self):
        def connection(db_function):
            def wrapper(*args):
                if self.mode not in ("read", "write", "read-write"):
                    logger_error.error(f"Invalid Operation type {self.mode} called for the function")
                else:
                    if self.mode == "read":
                        self.mode = "r"
                    elif self.mode == "write":
                        self.mode = "w"
                    elif self.mode == "read-write":
                        self.mode = "r+"
                with open(self.file_name, self.mode) as file_instance:
                    return db_function(file_instance, *args)
            return wrapper
        return connection