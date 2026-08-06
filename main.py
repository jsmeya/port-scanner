# jSCAN port scanner by Justin Smeya

# Imports
import sys
import socket

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Creates a new endpoint and returns one socket object
# AF_INET means a communication of standard 32-bit, IPv4 addresses paired with port numbers. Supports hostnames as well.
# SOCK_STREAM means a reliable, connected byte stream (maps to TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(target: str, port: int) -> bool:
    try:
        conn = s.connect((target, port))
        return True
    except:
        return False

if len(sys.argv) == 2:
    target = sys.argv[1]
    for i in range(1, 65536):
        if scan(target, i):
            print(f"{GREEN}Port {i} is open.{RESET}")
        else:
            print(f"Port {i} is closed.")
else:
    print(f"{RED}ERROR: Not enough arguments. Please reference an IP address or hostname to scan.{RESET}")