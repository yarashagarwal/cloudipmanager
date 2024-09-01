from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.read_database import read_db_content # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore
from cloudipmanager.c_iptools.address_space_number_free_addresses_calculator import address_space_number_free_addresses_calculator # type: ignore
from ipaddress import IPv4Network

logs_info = Logger("Info", "logger_delete_from_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_delete_from_database")
logger_error = logs_error.get_logger()

db_read_write_connection = DbConnection("write")

@db_read_write_connection.open_connection()
def delete_from_database(read_write_file_instance, cidr_to_be_deleted):
    db_content = read_db_content()
    cidr_to_be_deleted = IPv4Network(cidr_to_be_deleted)
    for address_space in db_content.root.values():
        if cidr_to_be_deleted.subnet_of(address_space.cidr):
            for sub_address_space in address_space.cidr:
                if cidr_to_be_deleted == sub_address_space.cidr:
                        db_content.root.address_space.address_subspaces.pop(cidr_to_be_deleted)
                if cidr_to_be_deleted.subnet_of(sub_address_space.cidr):
                    for subnet in address_space.subnets.values():
                        subnet.cidr 
                