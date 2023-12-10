# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:54:04 2023

@author: G702306
"""

# import the socket library
import socket

# define a variable to the socket connection
s = socket.socket()
# prompt the user for a host name
host = input(str("Enter host address of sender : "))
# use the port no. 8080
port = 8081

# connect to the socket with the hostname and port no.
s.connect((host, port))
print(f"Connected to port {port}.. ")

# prompt the user for a filename
# to receive data from to a new file (.txt)
filename = input(str("Enter a filename for incoming file : "))
file = open(filename, 'wb') # make it writeable and in bytes
file_data = s.recv(1024) #read the file in bytes

print(file_data)
file.write(file_data) # write the data to the new file
file.close() # close the file
print("File received successfully!")