from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_initialize_address_space.initialize_address_space import initialize_address_space # type: ignore
from cloudipmanager.c_database_operations.sort_database import sort_db, sort_address_spaces # type: ignore


logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

def structure_validation_db(db_content):
    private_ip_ranges = default_ip_ranges.PRIVATE_IP_RANGES.value
    # Check if all Private Address spaces are present in the DB
    for ip_range in private_ip_ranges:
        if ip_range not in db_content.root.keys():
            initial_address_spaces = initialize_address_space() # get the initiazer data structure
            db_content.root[ip_range] = initial_address_spaces.root[ip_range] # add the missing object to the structure
            db_content = IpaddressDatabaseV4.model_validate(db_content)
    # Sort all the sub-address spaces inside each address-space, all subnets within each sub address space and each address inside each subnet
    db_content=sort_db(db_content)
    return db_content