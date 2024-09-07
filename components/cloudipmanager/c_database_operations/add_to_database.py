from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.read_database import read_db_content # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_iptools.address_space_number_free_addresses_calculator import address_space_number_free_addresses_calculator # type: ignore

logs_info = Logger("Info", "logger_add_to_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_add_to_database")
logger_error = logs_error.get_logger()
db_connection_read_write = DbConnection("read-write")


@db_connection_read_write.open_connection()
def add_to_db(db_read_write_instance, user_input_model: IpAddressSpaceV4 | IpAddressSubSpaceV4 | SubnetIpv4):
    db_content: IpaddressDatabaseV4  = read_db_content()
    # Add new address spaces to the DB
    for address_space_cidr, address_space_model in db_content.root.items(): # Iterate through top level address spaces
        if hasattr(user_input_model, "subnets"):  # If content to be added is of address space type
            try:
                if user_input_model.cidr.subnet_of(address_space_model.cidr) and sub_add_spaces_checks_before_add(address_space_model, user_input_model): 
                    address_space_model.address_subspaces[str(user_input_model.cidr)] = user_input_model
                    updated_num_of_available_addresses = address_space_number_free_addresses_calculator(address_space_model.address_subspaces, address_space_model.num_of_addresses)
                    address_space_model.num_of_available_addresses = updated_num_of_available_addresses
                    db_content.root[address_space_cidr] = address_space_model
                    break
            except TypeError:
                db_content = structure_validation_db(db_content)
            
        if hasattr(user_input_model, "ip_addresses"): # If the user input content is of type subnet space
            # try:
            for sub_address_space_cidr, sub_address_space_model in address_space_model.address_subspaces.items(): # Iterate through the sub address spaces
                if user_input_model.cidr.subnet_of(sub_address_space_model.cidr) and subnet_checks_before_add(sub_address_space_model, user_input_model):
                    sub_address_space_model.subnets[str(user_input_model.cidr)] = user_input_model
                    updated_num_of_subspace_available_addresses = address_space_number_free_addresses_calculator(sub_address_space_model.subnets, sub_address_space_model.num_of_addresses)
                    sub_address_space_model.num_of_available_addresses = updated_num_of_subspace_available_addresses
                    db_content.root[address_space_cidr].address_subspaces[sub_address_space_cidr] = sub_address_space_model
                    break
        if hasattr(user_input_model, "ipaddress")
    else:
        logger_error.error(f"The sub address space that could hold the range {str(user_input_model.cidr)} could not be found.")
            # except TypeError:
            #     db_content = structure_validation_db(db_content)
            
    db_content = structure_validation_db(db_content)
    json.dump(IpaddressDatabaseV4.model_dump(db_content), db_read_write_instance, indent=2)
    

def sub_add_spaces_checks_before_add(address_space_model, user_input_model) -> bool:
    check_result: bool = True
    # Check if the sub address space already exists
    if str(user_input_model.cidr) in address_space_model.address_subspaces.keys(): 
        check_result = False
    # Check if the sub address overlaps with an existing sub address space
    for address_sub_space in address_space_model.address_subspaces.values():
        if user_input_model.cidr.overlaps(address_sub_space.cidr):
            check_result = False
    return check_result

def subnet_checks_before_add(address_sub_space_model, user_input_model) -> bool:
    check_result: bool = True
    # Check if the subnet address space already exists
    if str(user_input_model.cidr) in address_sub_space_model.subnets.keys():
        check_result = False
    # Check if the subnet address overlaps with an existing subnet address space
    for subnet_model in address_sub_space_model.subnets.values():
        if user_input_model.cidr.overlaps(subnet_model.cidr):
            check_result = False
    return check_result