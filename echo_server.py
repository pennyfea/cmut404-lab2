#!/usr/bin/env python
import socket
import sys

# Create socket
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Port for socket and Host
PORT = 8002
HOST = 'localhost'

# bind the socket to host and port
sockfd.bind((HOST, PORT))
# become a server socket
sockfd.listen(5)

# Establish and accept connections woth client
(clientsocket, address) = sockfd.accept()
while True:

    print("Got connection from", address)
    # Recieve message from the client
    message = clientsocket.recv(2024)
    print("Server received: " + message.decode('utf-8'))
    reply = ("Server output: " + message.decode('utf-8'))
    if not message:
        print("Client has been disconnected.....")
        break
    # Display messags.
    clientsocket.sendall(str.encode(reply))

# Close the connection with the client
clientsocket.close()
