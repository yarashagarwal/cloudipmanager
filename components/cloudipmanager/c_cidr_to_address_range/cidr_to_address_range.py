import ipaddress

def cidr_to_address_range(address_range) -> ipaddress.IPv4Network:
    """Convert the CIDR notation to start and end IP address"""
    # Convert the CIDR notation to start and end IP address
    address_cidr = ipaddress.IPv4Network(address_range)
    return address_cidr