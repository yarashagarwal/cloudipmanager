from pydantic import BaseModel
from datetime import datetime
from typing import Optional,Any

class ipaddress(BaseModel):
    ipaddress: str
    description: str
    unique_resource_id: Optional[str]
    tags: Optional[list[Any]]
    
class subnet(BaseModel):
    id: int
    cidr: str
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    ip_addresses: Optional[list[ipaddress]]
    tags: Optional[list[Any]]

class ip_address_inventory(BaseModel):
    id: int
    cidr: str
    description: str
    createdDate: datetime 
    modifiedDate: datetime
    status: str
    subnets: list[subnet]
    tags: Optional[list[Any]]
    
    
    