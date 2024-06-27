from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4# type: ignore
from cloudipmanager.c_initialize_address_space.initialize_address_space import initialize_address_space # type: ignore



logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

db_connection_read = DbConnection("read")
db_connection_read_write = DbConnection("read-write")

def update_db(operation: str, ipam_content: dict) -> None:
    if operation not in ["add", "modify", "delete"]:
        logger_error.error(f"Invalid Operation - {operation} - type called for the function")
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

def db_structure_validation(db_content) -> dict:
    private_ip_ranges = default_ip_ranges.PRIVATE_IP_RANGES.value
    try:
    # Check if all Private Address spaces are prsent in the DB
        for address_space_block in db_content:
            address_space_model = IpAddressSpaceV4.model_validate(db_content[address_space_block])
            if address_space_model.cidr in private_ip_ranges:
                private_ip_ranges.remove(address_space_model.cidr) # should be empty if all ranges are present in the DB
        if len(private_ip_ranges) != 0: # If there are initial address space blocks that are missing from the DB
            initial_address_spaces = initialize_address_space() # get the initiazer data structure
            for initial_address_space in initial_address_spaces: # figure out which one is missing
                initial_address_space_model = IpAddressSpaceV4.model_validate(initial_address_spaces[initial_address_space])
                if initial_address_space_model.cidr in private_ip_ranges:
                    db_content[initial_address_space] = initial_address_space_model.model_dump() # add the missing object to the structure 
        # sort the dictionary before seding it for write
        db_content=db_sort(db_content)
    except TypeError:
        db_content = initialize_address_space()
    return db_content

def db_sort(db_content):
    keys_sorted = list(db_content)
    keys_sorted.sort()
    db_content_sorted_by_keys = {key:db_content[key] for key in keys_sorted}
    logger_info.info("Sorted the DB alphabetically")
    return db_content_sorted_by_keys

@db_connection_read_write.open_connection()
def add_to_db(db_read_write_instance, ipam_content: dict):
        db_content = read_db_content()
        db_content = db_structure_validation(db_content)
        json.dump(db_content, db_read_write_instance, indent=2)
        # if db_content is None:
        #     json.dump(ipam_content, db_read_write_instance, indent=2)
        # else:
        #     logger_error.error("Initialization was attempted on populated DB. This will replace the DB´s original configuration")


update_db("add",{})