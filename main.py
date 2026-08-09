# jSCAN port scanner by Justin Smeya

# Imports
import sys
import socket

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Function to scan the target and each respective port
# NOTE: Add catches for network errors later
def scan(target: str, port: int) -> bool:
    try:
        # Creates a new endpoint and returns one socket object
        # AF_INET means a communication of standard 32-bit, IPv4 addresses paired with port numbers. Supports hostnames as well.
        # SOCK_STREAM means a reliable, connected byte stream (maps to TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            # Sets up a network link using the specified IP/hostname and port.
            # Then attempts to connect to that link.
            conn = s.connect((target, port))
            return True
    except (socket.timeout, OSError):
        return False

# Arguments when running
if len(sys.argv) == 2:
    target = sys.argv[1]

    # Sequentially run the scan() function
    for i in range(1, 65536):
        if scan(target, i):
            print(f"{GREEN}Port {i} is open.{RESET}")
        else:
            print(f"Port {i} is closed.")
else: # Fallback for if the user does not specify any arguments
    print(f"{RED}ERROR: Not enough arguments. Please specify an IP address or hostname to scan.{RESET}")