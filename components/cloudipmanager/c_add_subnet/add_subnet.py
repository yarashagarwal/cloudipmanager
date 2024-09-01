from cloudipmanager.c_skeleton.model import SubnetIpv4 # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_iptools.address_space_to_size_calculator import cidr_to_size # type: ignore
from cloudipmanager.c_cidr_to_address_range.cidr_to_address_range import cidr_to_address_range # type: ignore
from cloudipmanager.c_database_operations.update_database import update_db # type: ignore
from uuid import uuid4
from datetime import datetime
import ipaddress

logs_info = Logger("Info", "logger_add_subnet")
logger_info = logs_info.get_logger()

logs_error = Logger("Error", "logger_add_subnet")
logger_error = logs_error.get_logger()

class  add_subnet:
    def __init__(self, new_subnet_cidr, new_subnet_description, new_subnet_status, new_subnet_tags):
        self.id = str(uuid4())
        self.cidr = new_subnet_cidr
        self.start_ip_address = cidr_to_address_range(str(new_subnet_cidr))[0]
        self.end_ip_address = cidr_to_address_range(str(new_subnet_cidr))[-1]
        self.subnet_mask = ipaddress.IPv4Network(self.cidr).netmask
        self.description = new_subnet_description
        self.createdDate = datetime.now()
        self.modifiedDate = datetime.now()
        self.status = new_subnet_status
        self.ip_addresses = {}
        self.num_of_addresses = cidr_to_size(new_subnet_cidr)
        self.num_of_available_addresses = self.num_of_addresses
        self.tags = new_subnet_tags
    
    def add(self):
        subnet_model = SubnetIpv4.model_validate(self.__dict__)
        update_db("add", subnet_model)

new_subnet = add_subnet("10.15.4.128/25","test subnet","Active",{"name" : "yarash"})
new_subnet.add()


        
        