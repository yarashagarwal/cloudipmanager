import ipaddress

def cidr_to_size(cidr):
    cidr = ipaddress.IPv4Network(cidr)
    number_of_addresses = cidr.num_addresses
    return number_of_addresses