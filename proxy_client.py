#!/usr/bin/env python
import socket
import requests

class Proxy_Client:

    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
    
    def client(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', self.port))

        data = "www.sknvibes.com"
        self.sock.sendall(data.encode())

        results = self.sock.recv(4096)
        print("This is the request: ")
        print(results)
        # self.sock.close()
        
if __name__ == '__main__':
        cli = Proxy_Client('localhost', 8005)
        print("Starting client......")
        cli.client()