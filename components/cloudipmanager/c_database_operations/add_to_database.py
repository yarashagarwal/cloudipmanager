from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.read_database import read_db_content # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_iptools.address_space_number_free_addresses_calculator import address_space_number_free_addresses_calculator # type: ignore

logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()
db_connection_read_write = DbConnection("read-write")

@db_connection_read_write.open_connection()
def add_to_db(db_read_write_instance, ipam_content: IpAddressSpaceV4 | IpAddressSubSpaceV4 | SubnetIpv4):
    db_content = read_db_content()
    # Add new address spaces to the DB
    if "subnets" in (ipam_content.model_dump()).keys():  # If content to be added is of address space type
        ipam_content_model = ipam_content
        try:
            for address_space in db_content.root:
                address_space_model = IpAddressSpaceV4.model_validate(db_content.root[address_space])
                if ipam_content_model.cidr.subnet_of(address_space_model.cidr):
                    if sub_add_spaces_checks(address_space_model, ipam_content_model): 
                        address_space_model.address_subspaces[str(ipam_content_model.cidr)] = ipam_content_model
                        updated_num_of_available_addresses = address_space_number_free_addresses_calculator(address_space_model.address_subspaces, address_space_model.num_of_addresses)
                        address_space_model.num_of_available_addresses = updated_num_of_available_addresses
                        db_content.root[str(address_space)] = address_space_model
                        continue
        except TypeError:
            db_content = structure_validation_db(db_content)
    if "ip_addresses" in (ipam_content.model_dump()).keys(): # If the ipma content is of sype subnet space
        ipam_content_model = ipam_content
        try:
            for address_space in db_content.root:
                address_space_model = IpAddressSpaceV4.model_validate(db_content.root[address_space])
                if ipam_content_model.cidr.subnet_of(address_space_model.cidr):
                    for address_sub_space in address_space_model.address_subspaces:
                        address_sub_space_model = IpAddressSubSpaceV4.model_validate(address_space_model.address_subspaces[address_sub_space])
                        if ipam_content_model.cidr.subnet_of(address_sub_space_model.cidr):
                            if subnet_checks(address_sub_space_model,ipam_content_model):
                                address_sub_space_model.subnets[str(ipam_content_model.cidr)] = ipam_content_model
                                updated_num_of_subspace_available_addresses = address_space_number_free_addresses_calculator(address_sub_space_model.subnets, address_sub_space_model.num_of_addresses)
                                address_sub_space_model.num_of_available_addresses = updated_num_of_subspace_available_addresses
                                db_content.root[str(address_space)] = address_space_model
        except:
            db_content = structure_validation_db(db_content)
            
    db_content = structure_validation_db(db_content)
    json.dump(IpaddressDatabaseV4.model_dump(db_content), db_read_write_instance, indent=2)
    

def sub_add_spaces_checks(address_space_model, ipam_content_model) -> bool:
    check_result: bool = True
    # Check if the sub address space already exists
    if str(ipam_content_model.cidr) in list(address_space_model.address_subspaces.keys()): 
        check_result: bool = False
    # Check if the sub address overlaps with an existing sub address space
    for address_sub_space in address_space_model.address_subspaces:
        if ipam_content_model.cidr.overlaps(address_sub_space.cidr):
            check_result: bool = False
    return check_result

def subnet_checks(address_sub_space_model, ipam_content_model) -> bool:
    check_result: bool = True
    # Check if the subnet address space already exists
    if str(ipam_content_model.cidr) in list(address_sub_space_model.subnets.keys()):
        check_result: bool = False
    # Check if the subnet address overlaps with an existing subnet address space
    for subnet_address_space in address_sub_space_model.subnets:
        if ipam_content_model.cidr.overlaps(subnet_address_space.cidr):
            check_result: bool = False
    return check_result