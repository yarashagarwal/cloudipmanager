from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpaddressDatabaseV4# type: ignore
from cloudipmanager.c_initialize_address_space.initialize_address_space import initialize_address_space # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore



logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()
db_connection_read = DbConnection("read")

@db_connection_read.open_connection()
def read_db_content(db_read_instance) -> dict:
    try:
        db_content = json.load(db_read_instance)
        db_content = IpaddressDatabaseV4.model_validate(db_content)
    except json.decoder.JSONDecodeError:
        logger_error.error("The file content is empty. The DB must be initialized first")
        db_content = IpaddressDatabaseV4.model_validate({})
        db_content = structure_validation_db(db_content)
    return db_content