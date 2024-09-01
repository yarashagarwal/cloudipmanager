from cloudipmanager.c_skeleton.default_global_variables import global_variables # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore

logs_error = Logger("Error", "logger_db_connection")
logger_error = logs_error.get_logger()

class DbConnection:
    def __init__(self, mode):
        self.file_name=global_variables.DB_FILE
        self.mode = mode
        
    def open_connection(self): #This class instance function is called and the connection function is returned and therefore the connection function really becomes the decorator function
        def connection(db_function): # This is the actual decorator function which then decorates the db_function
            def wrapper(*args): # This is the wrapper function which replaces the decorated function
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
                    return db_function(file_instance, *args) # db_function is called with file_instance and the arguments
                    # the first argument of every function that is decorated with this function, must be the file instance, which can then be used inside the decorated function
            return wrapper
        return connection