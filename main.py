# Port scanner by Justin Smeya

import socket

# IP and port to scan
HOST = "45.33.32.156" #scanme.nmap.org

"""
AF_INET (default) means "Address Family, Internet."
It tells the OS socket interface that we're using standard, 32-bit IPv4 addresses + port numbers.
It uses a pair (host, port).

SOCK_STREAM (default) means a two-way byte stream socket type.
It uses TCP, so guarantees data order and safety.
No fixed packet/record boundaries.
Allows both sides to send/receive data simultaneously.
"""

for p in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect((HOST, p))