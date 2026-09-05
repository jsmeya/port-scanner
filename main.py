# Simple CLI port scanner by Justin Smeya

# Imports
import os
import socket
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import argparse

# Colors :)
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Function to scan the target and each respective port
def scan(target: str, port: int, timeout: float) -> tuple[bool, int]:
    try:
        # AF_INET = IPv4 (supports hostnames too)
        # SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port)) # Attempts to connect to network link
            return True, port
    except (socket.timeout, OSError):
        return False, port

# Parses a ports argument like "80,443" or "1-1024" or "22,80,1000-2000" into a sorted list of ports
def parse_ports(value: str) -> list[int]:
    ports = set()
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start, end = int(start_str), int(end_str)
            if start > end:
                raise argparse.ArgumentTypeError(f"Invalid port range: '{part}' (start must be <= end)")
            ports.update(range(start, end + 1))
        else:
            ports.add(int(part))

    if any(port < 1 or port > 65535 for port in ports):
        raise argparse.ArgumentTypeError("Ports must be between 1 and 65535")

    return sorted(ports)


# Upper bound on threads regardless of CPU count, to avoid crazy pool sizes
MAX_WORKERS = 1000

def worker_count(value: str) -> int:
    ivalue = int(value)
    if not (1 <= ivalue <= MAX_WORKERS):
        raise argparse.ArgumentTypeError(f"Workers must be between 1 and {MAX_WORKERS}, got {ivalue}")
    return ivalue

max_timeout = 5
def bounded_timeout(value: str) -> float:
    fvalue = float(value)
    if not (0 < fvalue <= max_timeout):
        raise argparse.ArgumentTypeError(f"Timeout must be between 0 and {max_timeout} seconds, got {fvalue}")
    return fvalue

default_workers = min(MAX_WORKERS, (os.cpu_count() or 4) * 50)

# Parsing arguments
def parse_args():
    # Initializing the parser
    parser = argparse.ArgumentParser(
        usage="%(prog)s [target (IP/HOSTNAME)] [-p PORTS] [-w WORKERS] [-t TIMEOUT] [-h (help)]",
        description="A basic, threaded TCP port scanner."
    )

    # Target IP address or hostname
    parser.add_argument(
        "target",
        help="IP address or hostname to scan."
    )

    # Ports / port ranges
    parser.add_argument(
        "-p", "--ports",
        type=parse_ports,
        default="1-65535",
        help="Ports to scan, e.g. '80,443' or '1-1024' or '22,80,1000-2000'. Defaults to all ports."
    )

    # Thread pool size
    parser.add_argument(
        "-w", "--workers",
        type=worker_count,
        default=default_workers,
        help=f"Number of worker threads (1-{MAX_WORKERS}). Defaults to a multiple of CPU cores ({default_workers} on this machine)."
    )

    # Socket timeout (s)
    parser.add_argument(
        "-t", "--timeout",
        type=bounded_timeout,
        default=1,
        help=f"Timeout interval, in seconds, for an attempted connection (0-{max_timeout})."
    )

    return parser.parse_args()

def main():
    args = parse_args()

    # Resolve host once upfront to make sure it's a real host.
    # Kind of like a ping, I suppose
    try:
        resolved_target = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"{RED}ERROR: Could not resolve target '{args.target}'.{RESET}")
        raise SystemExit(1)

    print(f"{BLUE}Scanning '{args.target}'...{RESET}\n")

    # Scan ports
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = executor.map(scan, repeat(resolved_target), args.ports, repeat(args.timeout))

    for result, port in results:
        if result == True:
            print(f"{GREEN}Port {port} is open.{RESET}")
        # elif result == False:
        #     print(f"Port {port} is closed.")
    print("Any ports not listed are closed, filtered, or listen over UDP and not TCP.")

if __name__ == "__main__":
    main()
