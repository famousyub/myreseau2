# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:53:53 2023

@author: G702306
"""

# import the socket library
import socket

# define a variable to the socket
s = socket.socket()

# get the hostname and add it to the socket
host = socket.gethostname()
host="localhost"
# use the port no. 8080
port = 8081
# bind the host and port no. to the socket
s.bind((host, port))

# listen to incoming connections
#s.listen(1)
s.listen()


# for the sake of easy connection
# print the host name of the user
print(host)
print(f"Waiting for incoming connections on port {port}..")
# when it receives a call, accept the conection
conn, addr = s.accept()
print(addr, "has connected to the server.")

# prompts the user to write the name of the file
# they want to transfer
filename = input(str("Enter name of the file :  "))
file = open(filename, 'rb') # make it readable and in bytes
file_data = file.read(1024) # read it in bytes
conn.send(file_data) # send the file data in bytes
print("Data transmitted successfully!")