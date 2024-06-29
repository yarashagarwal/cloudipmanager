import ipaddress
def sort_address_spaces_list(address_spaces_list: list) -> list:
    address_space_dict: dict = {}
    for address_space in address_spaces_list:
        address = address_space.split("/")[0]
        address_decimal = ipaddress.ip_address(address)
        address_space_dict[address_decimal] = address_space
    keys = list(address_space_dict.keys())
    keys.sort()
    address_space_dict_sorted = {k: address_space_dict[k] for k in keys}
    sorted_list: list = list(address_space_dict_sorted.values())
    return sorted_list