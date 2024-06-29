from cloudipmanager.c_db_connection.db_connection import DbConnection # type: ignore
import json
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_database_operations.read_database import read_db_content # type: ignore
from cloudipmanager.c_database_operations.structure_validation_database import structure_validation_db # type: ignore
from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, IpAddressSubSpaceV4, SubnetIpv4, IpaddressDatabaseV4 # type: ignore

logs_info = Logger("Info", "logger_update_database")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_update_database")
logger_error = logs_error.get_logger()
db_connection_read_write = DbConnection("read-write")

@db_connection_read_write.open_connection()
def add_to_db(db_read_write_instance, ipam_content: IpAddressSpaceV4 | IpAddressSubSpaceV4 | SubnetIpv4):
    db_content = read_db_content()
    # Add new address spaces to the DB
    if "subnets" in (ipam_content.model_dump()).keys(): 
        ipam_content_model = ipam_content
        try:
            for address_space in db_content.root:
                address_space_model = IpAddressSpaceV4.model_validate(db_content.root[address_space])
                if ipam_content_model.cidr.subnet_of(address_space_model.cidr):
                    if sub_add_spaces_checks(address_space_model, ipam_content_model): 
                        address_space_model.address_subspaces[str(ipam_content_model.cidr)] = ipam_content_model
                        db_content.root[str(address_space)] = address_space_model
                        continue
        except TypeError:
            db_content = structure_validation_db(db_content)
    db_content = structure_validation_db(db_content)
    json.dump(IpaddressDatabaseV4.model_dump(db_content), db_read_write_instance, indent=2)
    

def sub_add_spaces_checks(address_space_model, ipam_content_model) -> bool:
    # Check if the sub address space already exists
    if str(ipam_content_model.cidr) in list(address_space_model.address_subspaces.keys()): 
        check_result: bool = False
    else:
        check_result: bool = True
    return check_result