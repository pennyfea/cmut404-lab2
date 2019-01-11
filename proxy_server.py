#!/usr/bin/env python
import socket
class Proxy_Server:

    def __init__(self, HOST, PORT):

        self.host = HOST
        self.port = PORT

        # Create socket
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a host & port
        self.sockfd.bind((self.host,self.port))

        # become a server socket
        self.sockfd.listen(5)

        # Establish and accept connections with client
        (clientsocket, self.address) = self.sockfd.accept()

socket1 = Proxy_Server('localhost', 8001)
print("Got connection: ", socket1.address)