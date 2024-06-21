from components.cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges,global_variables # type: ignore
from cloudipmanager.c_skeleton.model import ip_address_inventory, subnet # type: ignore
from cloudipmanager.c_cidr_to_address_range.cidr_to_address_range import cidr_to_address_range # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore
from uuid import uuid4
from datetime import datetime
from pprint import pprint

logs_info = Logger("INFO", "logger_initialize_addresss_space")
logger_info = logs_info.get_logger()

def initialize_address_space() -> dict:
    """Initialize the address space with default values"""
    # Initialize the address space with default values
    initial_configuration: dict = {}
    address_space_id_class_A = str(uuid4())
    address_space_id_class_B = str(uuid4())
    address_space_id_class_C = str(uuid4())
    
    address_space_cidr_class_A = default_ip_ranges.CLASS_A_PRIVATE_IP_RANGE.value
    address_space_range_class_A = cidr_to_address_range(address_space_cidr_class_A)
    start_address_class_A = address_space_range_class_A[0]
    end_address_class_A = address_space_range_class_A[-1]
    
    address_space_cidr_class_B = default_ip_ranges.CLASS_B_PRIVATE_IP_RANGE.value
    address_space_range_class_B = cidr_to_address_range(address_space_cidr_class_B)
    start_address_class_B = address_space_range_class_B[0]
    end_address_class_B = address_space_range_class_B[-1]
    
    address_space_cidr_class_C = default_ip_ranges.CLASS_C_PRIVATE_IP_RANGE.value
    address_space_range_class_C = cidr_to_address_range(address_space_cidr_class_C)
    start_address_class_C = address_space_range_class_C[0]
    end_address_class_C = address_space_range_class_C[-1]
    
    description_class_A: str = "Class A private IP address space"
    description_class_B: str = "Class B private IP address space"
    description_class_C: str = "Class C private IP address space"
    
    created_date: str = str(datetime.now())
    modified_date: str= str(datetime.now())
    
    initial_subnets: list[subnet] = []
    
    status = "Active"
    
    address_space_class_A = ip_address_inventory(
                                        id=address_space_id_class_A,
                                        cidr=address_space_cidr_class_A,
                                        start_ip_address=str(start_address_class_A),
                                        end_ip_address = str(end_address_class_A),
                                        description = description_class_A,
                                        createdDate = created_date,
                                        modifiedDate = modified_date,
                                        status = status,
                                        subnets = initial_subnets,
                                        tags=None
                                        )
    address_space_class_B = ip_address_inventory(
                                        id=address_space_id_class_B,
                                        cidr=address_space_cidr_class_B,
                                        start_ip_address=str(start_address_class_B),
                                        end_ip_address = str(end_address_class_B),
                                        description = description_class_B,
                                        createdDate = created_date,
                                        modifiedDate = modified_date,
                                        status = status,
                                        subnets = initial_subnets,
                                        tags=None
                                        )
    
    address_space_class_C = ip_address_inventory(
                                        id=address_space_id_class_C,
                                        cidr=address_space_cidr_class_C,
                                        start_ip_address=str(start_address_class_C),
                                        end_ip_address = str(end_address_class_C),
                                        description = description_class_C,
                                        createdDate = created_date,
                                        modifiedDate = modified_date,
                                        status = status,
                                        subnets = initial_subnets,
                                        tags=None
                                        )
    
    logger_info.info("Creating initial address space entries")
    initial_configuration["address_space_class_A"] = dict(address_space_class_A)
    initial_configuration["address_space_class_B"] = dict(address_space_class_B)
    initial_configuration["address_space_class_C"] = dict(address_space_class_C)
    return initial_configuration


initial_configuration = initialize_address_space()
pprint(initial_configuration)