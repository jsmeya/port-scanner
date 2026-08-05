# jSCAN port scanner by Justin Smeya

# Imports
import sys

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

if len(sys.argv) == 2:
    print(f"{GREEN}Now scanning: {sys.argv[1]}{RESET}")
else:
    print(f"{RED}Invalid arguments. Please provide an IP address or hostname to scan.{RESET}")