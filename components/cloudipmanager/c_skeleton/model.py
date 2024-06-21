from pydantic import BaseModel
from typing import Optional

class ipaddress(BaseModel):
    ipaddress: str
    description: str
    unique_resource_id: Optional[str]
    tags: Optional[dict[str,str]]
    
class subnet(BaseModel):
    id: str
    cidr: str
    start_ip_address: str
    end_ip_address: str
    subnet_mask: str
    description: str
    createdDate: str
    modifiedDate: str
    status: str
    ip_addresses: Optional[list[ipaddress]]
    tags: Optional[dict[str,str]]

class ip_address_inventory(BaseModel):
    id: str
    cidr: str
    start_ip_address: str
    end_ip_address: str
    description: str
    createdDate: str 
    modifiedDate: str
    status: str
    subnets: list[subnet]
    tags: Optional[dict[str,str]]
    
    
    