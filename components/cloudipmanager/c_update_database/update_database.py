from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore

logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

db_connection_read = DbConnection("r")
db_connection_read_write = DbConnection("r+")

def update_db(operation: str, ipam_content: dict) -> None:
    if operation not in ("add", "modify", "delete"):
        logger_error.error("Invalid Operation type called for the function")
    if operation.lower() == "add":
        add_to_db(ipam_content)

@db_connection_read.open_connection()
def read_db_content(db_read_instance) -> dict:
    try:
        db_content = json.load(db_read_instance)
    except json.decoder.JSONDecodeError:
        logger_error.error("The file content is empty. The DB must be initialized first")
        db_content = None
    return db_content

@db_connection_read_write.open_connection()
def add_to_db(db_read_write_instance, ipam_content: dict):
        db_content = read_db_content()
        if db_content is None:
            json.dump(ipam_content, db_read_write_instance, indent=2)
