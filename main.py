# jSCAN port scanner by Justin Smeya

# Imports
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
target = "scanme.nmap.org"

def scan(port: int) -> bool:
    try:
        conn = s.connect((target, port))
        return True
    except:
        return False

# Getting a target server
for i in range(1, 65536):
    if scan(i):
        print(f"Port {i} is open.")