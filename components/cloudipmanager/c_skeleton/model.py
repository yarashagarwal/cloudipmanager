from pydantic import BaseModel, field_serializer
from typing import Optional
from ipaddress import IPv4Network, IPv4Address
from datetime import datetime

class IpaddressV4(BaseModel):
    ipaddress: IPv4Address
    description: str
    unique_resource_id: Optional[str]
    tags: Optional[dict[str,str]]
    
    @field_serializer('ipaddress')
    def serialize_ipaddress(self, ipaddress: IPv4Address):
        return str(ipaddress)
    
class SubnetIpv4(BaseModel):
    id: str
    cidr: IPv4Network
    start_ip_address: IPv4Address
    end_ip_address: IPv4Address
    subnet_mask: str
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    ip_addresses: Optional[list[IpaddressV4]]
    tags: Optional[dict[str,str]]
    
    @field_serializer('cidr')
    def serialize_cidr(self, cidr: IPv4Network):
        return str(cidr)
    
    @field_serializer('start_ip_address')
    def serialize_start_ip_address(self, start_ip_address: IPv4Address):
        return str(start_ip_address)
    
    @field_serializer('end_ip_address')
    def serialize_end_ip_address(self, end_ip_address: IPv4Address):
        return str(end_ip_address)
    
    @field_serializer('createdDate')
    def serialize_createdDate(self, createdDate: datetime):
        return str(createdDate)
    
    @field_serializer('modifiedDate')
    def serialize_modifiedDate(self, modifiedDate: datetime):
        return str(modifiedDate)

class IpAddressSpaceV4(BaseModel):
    id: str
    cidr: IPv4Network
    start_ip_address: IPv4Address
    end_ip_address: IPv4Address
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    subnets: list[SubnetIpv4]
    tags: Optional[dict[str,str]]
    
    @field_serializer('cidr')
    def serialize_cidr(self, cidr: IPv4Network):
        return str(cidr)
    
    @field_serializer('start_ip_address')
    def serialize_start_ip_address(self, start_ip_address: IPv4Address):
        return str(start_ip_address)
    
    @field_serializer('end_ip_address')
    def serialize_end_ip_address(self, end_ip_address: IPv4Address):
        return str(end_ip_address)
    
    @field_serializer('createdDate')
    def serialize_createdDate(self, createdDate: datetime):
        return str(createdDate)
    
    @field_serializer('modifiedDate')
    def serialize_modifiedDate(self, modifiedDate: datetime):
        return str(modifiedDate)