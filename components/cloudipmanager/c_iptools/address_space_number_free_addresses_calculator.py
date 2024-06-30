def address_space_number_free_addresses_calculator(address_spaces: dict, num_of_addresses) -> int:
    available_address_spaces = num_of_addresses
    for address_space in address_spaces:
        available_address_spaces = available_address_spaces - address_spaces[address_space].num_of_addresses
    
    return available_address_spaces