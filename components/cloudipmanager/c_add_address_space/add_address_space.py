from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, SubnetIpv4 # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore
from cloudipmanager.c_cidr_to_address_range.cidr_to_address_range import cidr_to_address_range # type: ignore
from uuid import uuid4

logs_info = Logger("Info", "logger_add_subnet")
logger_info = Logger.get_logger()

logs_error = Logger("Error", "logger_add_subnet")
logger_error = logs_error.get_logger()

def add_address_space() -> dict:
    new_address_space_id: str = str(uuid4())
    new_address_space_cidr: 
    new_address_space_start_ip_address
    new_address_space_end_ip_address
    new_address_space_description
    new_address_space_created_date
    new_address_space_modified_date
    new_address_space_status
    new_address_space_subnets
    return new_address_space