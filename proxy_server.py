#!/usr/bin/env python
import socket
import os
import sys
from multiprocessing import Process

class Proxy_Server:

    def __init__(self, HOST, PORT):

        self.host = HOST
        self.port = PORT

    
    def server(self):
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to host and port
        self.sock.bind((self.host, self.port))
        # Start listening
        self.sock.listen(5)

        while True:
            # Accept the connection
            clientsocket, address = self.sock.accept()

            #Spawn multiple processes
            process = Process(target = self.handle_connection, args = (clientsocket, address))
            process.daemon = True
            process.start()

    def handle_connection(self, conn, address):

        print("Got connection from", address)

        while True:

            process_id = os.getpid()
            print("Process id:", process_id)

            # Recieve message from the client
            message = conn.recv(2024)

            hostname = message.decode('utf-8').rstrip('\n').rstrip('\r')

            try:
                host_ip = socket.gethostbyname(hostname)
            except socket.gaierror:
                print("Error with resolving host name")
            # print(host_ip)

            # Requests a page
            request = "GET / HTTP/1.1\r\nHost: " + host_ip + "\n\n"

            conn.sendall(request.encode())
        conn.close()

if __name__ == '__main__':
        ser = Proxy_Server('localhost', 8005)
        print("Starting server......")
        ser.server()