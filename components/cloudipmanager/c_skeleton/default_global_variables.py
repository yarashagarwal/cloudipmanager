from enum import Enum

class default_ip_ranges(Enum):
    """Default IP ranges for the private address space"""
    CLASS_A_PRIVATE_IP_START = "10.0.0.0"
    CLASS_A_PRIVATE_IP_END = "10.255.255.255"
    CLASS_B_PRIVATE_IP_START = "172.16.0.0"
    CLASS_B_PRIVATE_IP_END = "172.31.255.255"
    CLASS_C_PRIVATE_IP_START = "192.168.0.0"
    CLASS_C_PRIVATE_IP_END = "192.168.255.255"
    
    def __str__(self):
        return "CLASS_A_PRIVATE_IP_RANGE" + ": " + self.CLASS_A_PRIVATE_IP_START.value + " - " + self.CLASS_A_PRIVATE_IP_END.value + "\n" + \
                "CLASS_B_PRIVATE_IP_RANGE" + ": " + self.CLASS_B_PRIVATE_IP_START.value + " - " + self.CLASS_B_PRIVATE_IP_END.value + "\n" + \
                "CLASS_C_PRIVATE_IP_RANGE" + ": " + self.CLASS_C_PRIVATE_IP_START.value + " - " + self.CLASS_C_PRIVATE_IP_END.value
