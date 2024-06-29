from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_initialize_address_space.initialize_address_space import initialize_address_space # type: ignore
from cloudipmanager.c_database_operations.sort_database import sort_db, sort_address_spaces # type: ignore


logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

def structure_validation_db(db_content) -> dict:
    private_ip_ranges = default_ip_ranges.PRIVATE_IP_RANGES.value
    # Check if all Private Address spaces are prsent in the DB
    for address_space_block in db_content.root:
        address_space_model = IpAddressSpaceV4.model_validate(db_content.root[address_space_block])
        if str(address_space_model.cidr) in private_ip_ranges:
            private_ip_ranges.remove(str(address_space_model.cidr)) # should be empty if all ranges are present in the DB
    if len(private_ip_ranges) != 0: # If there are initial address space blocks that are missing from the DB
        initial_address_spaces = initialize_address_space() # get the initiazer data structure
        initial_address_spaces_model = IpaddressDatabaseV4.model_validate(initial_address_spaces)
        for initial_address_space in initial_address_spaces_model.root: # figure out which one is missing
            initial_address_space_model = IpAddressSpaceV4.model_validate(initial_address_spaces.root[initial_address_space])
            if str(initial_address_space_model.cidr) in private_ip_ranges:
                db_content.root[initial_address_space] = initial_address_space_model # add the missing object to the structure
    # Sort all the sub-address spaces inside each address-space
    for address_space_block in db_content.root:
        address_space_model = IpAddressSpaceV4.model_validate(db_content.root[address_space_block])
        address_space_model_sorted_sub_address_spaces = sort_address_spaces(address_space_model.address_subspaces)
        address_space_model.address_subspaces = address_space_model_sorted_sub_address_spaces
        db_content.root[address_space_block] = address_space_model
    # sort the dictionary before seding it for write
    db_content=sort_db(db_content)
    return db_content