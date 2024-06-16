from pydantic import BaseModel
from datetime import datetime
from components.cloudipmanager.c_initialize_address_space.default_global_variables import default_ip_ranges

class subnet(BaseModel):
    id: int
    cidr: str
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    ip_address_inventory_id: int

class ip_address_inventory(BaseModel):
    id: int
    cidr: str
    description: str
    createdDate: datetime 
    modifiedDate: datetime
    status: str
    subnets: list[subnet]
    
    
    