from pydantic import BaseModel
from typing import Optional

class IpaddressV4(BaseModel):
    ipaddress: str
    description: str
    unique_resource_id: Optional[str]
    tags: Optional[dict[str,str]]
    
class SubnetIpv4(BaseModel):
    id: str
    cidr: str
    start_ip_address: str
    end_ip_address: str
    subnet_mask: str
    description: str
    createdDate: str
    modifiedDate: str
    status: str
    ip_addresses: Optional[list[IpaddressV4]]
    tags: Optional[dict[str,str]]

class IpAddressSpaceV4(BaseModel):
    id: str
    cidr: str
    start_ip_address: str
    end_ip_address: str
    description: str
    createdDate: str 
    modifiedDate: str
    status: str
    subnets: list[SubnetIpv4]
    tags: Optional[dict[str,str]]