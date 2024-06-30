from cloudipmanager.c_skeleton.model import IpAddressSubSpaceV4 # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_iptools.address_space_to_size_calculator import cidr_to_size # type: ignore
from cloudipmanager.c_cidr_to_address_range.cidr_to_address_range import cidr_to_address_range
from cloudipmanager.c_database_operations.update_database import update_db # type: ignore
from uuid import uuid4
from datetime import datetime

logs_info = Logger("Info", "logger_add_address_sub_space")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_add_address_sub_space")
logger_error = logs_error.get_logger()

class  add_address_space:
    def __init__(self, new_address_sub_space_cidr, new_address_sub_space_description, new_address_sub_space_status, new_address_space_tags):
        self.id = str(uuid4())
        self.cidr = new_address_sub_space_cidr
        self.start_ip_address = cidr_to_address_range(str(new_address_sub_space_cidr))[0]
        self.end_ip_address = cidr_to_address_range(str(new_address_sub_space_cidr))[-1]
        self.description = new_address_sub_space_description
        self.createdDate = datetime.now()
        self.modifiedDate = datetime.now()
        self.status = new_address_sub_space_status
        self.subnets = {}
        self.num_of_addresses = cidr_to_size(new_address_sub_space_cidr)
        self.num_of_available_addresses = self.num_of_addresses
        self.tags = new_address_space_tags
    
    def add(self):
        address_sub_space_model = IpAddressSubSpaceV4.model_validate(self.__dict__)
        update_db("add", address_sub_space_model)

new_address_space = add_address_space("10.15.1.0/24","test subnet","Active",{"name" : "yarash"})
new_address_space.add()


        
        