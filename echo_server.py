#!/usr/bin/env python
import socket
import os
import sys
from multiprocessing import Process

def handle_connection(accepted_socket, address):

        process_id = os.getpid()
        print("Process id:", process_id)

        print("Got connection from", address)
        # Recieve message from the client

        message = accepted_socket.recv(2024)
        print("Server received: " + message.decode('utf-8'))
        reply = ("Server output: " + message.decode('utf-8'))
        if not message:
                print("Client has been disconnected.....")
                # Close the connection with the client
                accepted_socket.close()
                sys.exit()
        # Display messags.
        accepted_socket.sendall(str.encode(reply))

 
        

def server():

        # Port for socket and Host
        HOST = 'localhost'
        PORT = 8001
        
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to host and port
        sock.bind((HOST, PORT))
        # become a server socket
        sock.listen(5)
        
        while True:
                 # blocks here.
                clientsocket, address = sock.accept()
                # unblocked 
                client_process = Process(target=handle_connection, args=(clientsocket, address))
                client_process.start()

if __name__ == '__main__':
    server()