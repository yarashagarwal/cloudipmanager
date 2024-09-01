from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.add_to_database import add_to_db 
from cloudipmanager.c_database_operations.delete_from_database import delete_from_database # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSubSpaceV4, IpAddressSpaceV4, SubnetIpv4 # type: ignore



logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()


def update_db(operation: str, ipam_content: IpAddressSpaceV4 | IpAddressSubSpaceV4 | SubnetIpv4 = {}, cidr_to_be_deleted: str = "0.0.0.0/0") -> None:
    if operation not in ["add", "modify", "delete"]:
        logger_error.error(f"Invalid Operation - {operation} - type called for the function")
    if operation.lower() == "add":
        add_to_db(ipam_content)
    if operation.lower() == "delete":
        delete_from_database(cidr_to_be_deleted)
        

