# Simple CLI port scanner by Justin Smeya

# Imports
import sys
import socket
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Function to scan the target and each respective port
def scan(target: str, port: int) -> tuple[bool, int]:
    try:
        # AF_INET = IPv4 (supports hostnames too)
        # SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((target, port)) # Attempts to connect to network link
            return True, port
    except (socket.timeout, OSError):
        return False, port

# Variables
port_range = range(1, 65536)
max_workers = 100

# Arguments when running
if len(sys.argv) == 2:
    target = sys.argv[1]
    print(f"{BLUE}Scanning '{target}'...{RESET}\n")

    # Scan ports
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(scan, repeat(target), port_range)

    for result, port in results:
        if result == True:
            print(f"{GREEN}Port {port} is open.{RESET}")
        elif result == False:
            print(f"Port {port} is closed.")

else: # Fallback for if the user does not specify any arguments
    print(f"{RED}ERROR: Not enough arguments. Please specify an IP address or hostname to scan.{RESET}")