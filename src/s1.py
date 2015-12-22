#!/usr/bin/python           # This is server.py file
import redis
import socket               # Import socket module
import re

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
s = socket.socket()         # Create a socket object
host = 'localhost'          # Get local machine name
port = 8080                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.settimeout(10)
s.listen(5)                 # Now wait for client connection.

while True:
	c, addr = s.accept()     # Establish connection with client.
	message = re.findall(r'\b\d+\b', str(c.recv(1024),'UTF-8'))
	itemUser = message[0] + ':' + message[1] + ':' + message[2]
	print(itemUser)
	r1.lpush('qiu', itemUser) 
	#print (itemUser)
	#print (message[0])
	#print (message[1])	
	c.close()                # Close the connection
