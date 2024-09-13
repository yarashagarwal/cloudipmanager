from cloudipmanager.c_skeleton.model import IpaddressV4 # type: ignore
from cloudipmanager.c_database_operations.update_database import update_db  # type: ignore
from uuid import uuid4

class add_ip_address:
    def __init__(self, new_ip_address: str, new_ip_address_description: str, new_ip_address_tags: dict):
        self.ip_address = new_ip_address
        self.description = new_ip_address_description
        self.unique_resource_id = str(uuid4())
        self.tags = new_ip_address_tags
        
    def add(self):
        ip_address_model = IpaddressV4.model_validate(self.__dict__)
        update_db("add",ip_address_model)
        
new_ip_address = add_ip_address("10.15.5.3", "First IP address of the subnet", {"usage": "none"})
new_ip_address.add()