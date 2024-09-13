from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4, IpaddressV4 # type: ignore  # type: ignore

logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()

def sort_db(db_content: IpaddressDatabaseV4):
    db_content_dict=IpaddressDatabaseV4.model_dump(db_content)
    sorted_address_spaces = sort_address_spaces(db_content_dict)
    sorted_db_content = IpaddressDatabaseV4.model_validate(sorted_address_spaces)
    return sorted_db_content

def sort_address_spaces(db_content_dict: dict[str,IpAddressSpaceV4]):
    address_spaces_keys = list(db_content_dict)
    address_spaces_keys.sort()
    sorted_address_spaces = {address_spaces_key:db_content_dict[address_spaces_key] for address_spaces_key in address_spaces_keys}
    #Sorted top level address spaces here and continue with sorting the sub address spaces
    for address_space in sorted_address_spaces:
        sorted_address_spaces[address_space]["address_subspaces"] = sort_address_subspaces(sorted_address_spaces[address_space]["address_subspaces"])
    logger_info.info("Sorted the DB address spaces alphabetically")
    return sorted_address_spaces

def sort_address_subspaces(address_subspaces: dict[str,IpAddressSubSpaceV4]):
    address_subspaces_keys = list(address_subspaces)
    address_subspaces_keys.sort()
    address_subspaces_sorted = {address_subspace_key: address_subspaces[address_subspace_key] for address_subspace_key in address_subspaces_keys}
    # SOrted address_subscpaces. MOving on to sorting the subnets inside each address subspace
    for address_subspace in address_subspaces_sorted:
        address_subspaces_sorted[address_subspace]["subnets"] = sort_subnets(address_subspaces_sorted[address_subspace]["subnets"])
    return address_subspaces_sorted

def sort_subnets(subnets: dict[str, SubnetIpv4]):
    subnets_keys=list(subnets)
    subnets_keys.sort()
    subnets_sorted = {subnets_key: subnets[subnets_key] for subnets_key in subnets_keys}
    # Sorted subnets. Next sorting IP addresses in a subnet
    for subnet in subnets_sorted:
        subnets_sorted[subnet]["ip_addresses"] = sort_ip_addresses(subnets_sorted[subnet]["ip_addresses"])
    return subnets_sorted

def sort_ip_addresses(ip_addresses: dict[str, IpaddressV4]):
    ip_address_keys = list(ip_addresses)
    ip_address_keys.sort()
    ip_addresses_sorted = {ip_address_key: ip_addresses[ip_address_key] for ip_address_key in ip_address_keys}
    return ip_addresses_sorted