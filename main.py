# Simple CLI port scanner by Justin Smeya

# Imports
import sys
import socket
from concurrent.futures import ThreadPoolExecutor

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

port_range = range(1, 65536)

# Function to scan the target and each respective port
def scan(target: str, port: int) -> bool:
    try:
        # AF_INET = IPv4 (supports hostnames too)
        # SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((target, port)) # Attempts to connect to network link
            return True
    except (socket.timeout, OSError):
        return False

# Arguments when running
if len(sys.argv) == 2:
    target = sys.argv[1]
    print(f"{BLUE}Scanning '{target}'...{RESET}\n")

    # Sequentially run the scan() function
    for i in port_range:
        if scan(target, i):
            print(f"{GREEN}Port {i} is open.{RESET}")
        else:
            print(f"Port {i} is closed.")
else: # Fallback for if the user does not specify any arguments
    print(f"{RED}ERROR: Not enough arguments. Please specify an IP address or hostname to scan.{RESET}")