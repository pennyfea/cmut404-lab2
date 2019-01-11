#!/usr/bin/env python
import socket
import os
import sys
from multiprocessing import Process

class Server:

        def __init__(self, HOST, PORT):
                 # Port for socket and Host
                self.hostname = HOST
                self.port = PORT
        
        def server(self):
                # Create socket
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # bind the socket to host and port
                self.sock.bind((self.hostname, self.port))
                # become a server socket
                self.sock.listen(5)

                while True:
                        # Accept the connection
                        clientsocket, address = self.sock.accept()

                        #Spawn multiple processes
                        process = Process(target = handle_connection, args = (clientsocket, address))
                        process.daemon = True
                        process.start()

def handle_connection(conn, address):

        print("Got connection from", address)

        while True:

                process_id = os.getpid()
                
                # Recieve message from the client
                message = conn.recv(2024)
                print("Process id:", process_id)
                print("Server received: " + message.decode('utf-8'))
                reply = ("Server output: " + message.decode('utf-8'))
                if not message:
                        print("Client has been disconnected.....")
                        break
                # Display messags
                conn.sendall(str.encode(reply))
        conn.close()

if __name__ == '__main__':
        ser = Server('localhost', 8003)
        print("Starting server......")
        ser.server()
     