#!/usr/bin/env python
import socket
import os
from multiprocessing import Process, current_process

def create_socket():

    # Get the process id.
    process_id = os.getpid()
    print("Process id:", process_id)

    # Create socket
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Port for socket and Host
    PORT = 8005
    HOST = 'localhost'

    # bind the socket to host and port
    sockfd.bind((HOST, PORT))
    # become a server socket
    sockfd.listen(5)

    # Establish and accept connections woth client
    (clientsocket, address) = sockfd.accept()

    start_socket(clientsocket,address)

def start_socket(clientsocket,address):
   
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

if __name__ == '__main__':

    processes = []
    process = Process(target = create_socket)
    processes.append(process)

    # Processes are spawned by creating a Process object and
    # then calling its start method
    process.start()