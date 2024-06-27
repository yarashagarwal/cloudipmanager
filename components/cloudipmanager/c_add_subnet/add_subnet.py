from cloudipmanager.c_skeleton.model import IpAddressSpaceV4, SubnetIpv4 # type: ignore
from cloudipmanager.c_logger.logger import Logger # type: ignore
from cloudipmanager.c_skeleton.default_global_variables import default_ip_ranges# type: ignore

logs_info = Logger("Info", "logger_add_subnet")
logger_info = Logger.get_logger()

logs_error = Logger("Error", "logger_add_subnet")
logger_error = logs_error.get_logger()

def add_subnet() -> dict:
    