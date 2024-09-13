from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.read_database import read_db_content # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore
from cloudipmanager.c_skeleton.model import IpaddressV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_iptools.address_space_number_free_addresses_calculator import address_space_number_free_addresses_calculator # type: ignore
from ipaddress import IPv4Network, IPv4Address

logs_info = Logger("Info", "logger_delete_from_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_delete_from_database")
logger_error = logs_error.get_logger()

db_read_write_connection = DbConnection("write")

@db_read_write_connection.open_connection()
def delete_from_database(read_write_file_instance, object_type_to_be_deleted: str, object_to_be_deleted: IPv4Network | IPv4Address):
    db_content = read_db_content()
    if object_type_to_be_deleted == "sub_address_space":
        db_content = delete_sub_address_space(object_to_be_deleted, db_content) #delete sub address space from one of the address spaces in the root
    if object_type_to_be_deleted == "subnet":
        db_content = delete_subnet(object_to_be_deleted, db_content) #delete sub address space from one of the address spaces in the root
    if object_type_to_be_deleted == "ip_address":
        db_content = delete_ip_address(object_to_be_deleted, db_content)
    
    db_content = structure_validation_db(db_content)
    json.dump(IpaddressDatabaseV4.model_dump(db_content), read_write_file_instance, indent=2)
    
        
def delete_sub_address_space(object_to_be_deleted: IPv4Network, db_content: IpaddressDatabaseV4) -> IpaddressDatabaseV4:
    for address_space_key in db_content.root:
        if object_to_be_deleted in db_content.root[address_space_key].address_subspaces:
                db_content.root[address_space_key].address_subspaces.pop(object_to_be_deleted)
    return db_content

def delete_subnet(object_to_be_deleted: IPv4Network, db_content: IpaddressDatabaseV4) -> IpaddressDatabaseV4:
    for address_space_key in db_content.root:
        for address_sub_space_key in address_space_key[address_space_key].address_subspaces:
            if object_to_be_deleted in db_content.root[address_space_key].address_subspaces[address_sub_space_key].subnets:
                db_content.root[address_space_key].address_subspaces[address_sub_space_key].subnets.pop(object_to_be_deleted)
    return db_content

def delete_ip_address(object_to_be_deleted: IPv4Address, db_content: IpaddressDatabaseV4) -> IpaddressDatabaseV4:
    for address_space in db_content.root:
        for address_subspace in db_content.root[address_space].address_subspaces:
            for subnet in db_content.root[address_space].address_subspaces[address_subspace].subnets:
                if object_to_be_deleted in db_content.root[address_space].address_subspaces[address_subspace].subnets[subnet].ip_addresses:
                    db_content.root[address_space].address_subspaces[address_subspace].subnets[subnet].ip_addresses.pop(object_to_be_deleted)
    return db_content