from pydantic import BaseModel, field_serializer, RootModel
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
    subnet_mask: IPv4Address
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    ip_addresses: Optional[dict[str,IpaddressV4]]
    num_of_addresses: int
    num_of_available_addresses: int
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
    
    @field_serializer('subnet_mask')
    def serialize_netmask(self, subnet_mask: IPv4Address):
        return str(subnet_mask)
class IpAddressSubSpaceV4(BaseModel):
    id: str
    cidr: IPv4Network
    start_ip_address: IPv4Address
    end_ip_address: IPv4Address
    description: str
    createdDate: datetime
    modifiedDate: datetime
    status: str
    subnets: Optional[dict[str,SubnetIpv4]]
    num_of_addresses: int
    num_of_available_addresses: int
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
    address_subspaces: Optional[dict[str,IpAddressSubSpaceV4]]
    num_of_addresses: int
    num_of_available_addresses: int
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

class IpaddressDatabaseV4(RootModel[dict[str, IpAddressSpaceV4]]):
    
    def model_dump(self, **kwargs):
        database_dictionary = super().model_dump(**kwargs)
        return  {str(k):v for k,v in database_dictionary.items()}