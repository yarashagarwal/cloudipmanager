from enum import Enum

class default_ip_ranges(Enum):
    """Default IP ranges for the private address space"""
    CLASS_A_PRIVATE_IP_RANGE = "10.0.0.0/8"
    CLASS_B_PRIVATE_IP_RANGE = "172.16.0.0/12"
    CLASS_C_PRIVATE_IP_RANGE = "192.168.0.0/16"
    
    def __str__(self):
        return "CLASS_A_PRIVATE_IP_RANGE" + ": " + self.CLASS_A_PRIVATE_IP_RANGE.value + " - " + "\n" + \
                "CLASS_B_PRIVATE_IP_RANGE" + ": " + self.CLASS_B_PRIVATE_IP_RANGE.value + " - " + "\n" + \
                "CLASS_C_PRIVATE_IP_RANGE" + ": " + self.CLASS_C_PRIVATE_IP_RANGE.value + " - "

class global_variables:
    """Global variables for the application"""
    LOG_LEVEL = "INFO"
    LOG_FILE = "cloudipmanager.log"
    DB_FILE = "ipconfig.json"