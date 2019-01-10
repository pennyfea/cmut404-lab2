#!/usr/bin/env python
import socket
import requests

# Create socket
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Port for socket
port = 80

# Get host IP
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("Error with resolving host name")


# Requests a page
request = "GET / HTTP/1.1\r\nHost: " + host_ip + "\n\n"

# connecting to the server
sockfd.connect((host_ip, port))


sockfd.send(request.encode())
result = sockfd.recv(4096)

print(result)
