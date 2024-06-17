
import ipaddress

def address_range_to_cidr(start_ip_address, end_ip_address):
    """Convert the start and end IP address to CIDR notation"""
    # Convert the start and end IP address to CIDR notation
    start_ip_address = ipaddress.ip_address(start_ip_address)
    end_ip_address = ipaddress.ip_address(end_ip_address)
    cidr = ipaddress.summarize_address_range(start_ip_address, end_ip_address)  
    return cidr