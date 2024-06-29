from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_iptools.sort_address_spaces_list import sort_address_spaces_list

logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

def sort_db(db_content: IpaddressDatabaseV4):
    db_content_dict=IpaddressDatabaseV4.model_dump(db_content)
    keys_sorted = list(db_content_dict)
    keys_sorted.sort()
    db_content_sorted_by_keys = {key:db_content_dict[key] for key in keys_sorted}
    db_content_sorted_by_keys = IpaddressDatabaseV4.model_validate(db_content_sorted_by_keys)
    logger_info.info("Sorted the DB alphabetically")
    return db_content_sorted_by_keys

def sort_address_spaces(address_spaces: dict[str,IpAddressSubSpaceV4]):
    cidrs = list(address_spaces.keys())
    cidrs_sorted = sort_address_spaces_list(cidrs)
    address_spaces = {address_space: address_spaces[address_space] for address_space in cidrs_sorted}
    return address_spaces