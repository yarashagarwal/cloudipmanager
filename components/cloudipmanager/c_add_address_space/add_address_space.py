from cloudipmanager.c_skeleton.model import ip_address_space
from uuid import uuid4

def add_address_space_ipv4(cidr,description,status,tags) -> ip_address_space:
    id = uuid4()
    cidr = cidr
    ip_address_range