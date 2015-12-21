#!/usr/bin/python           # This is client.py file
import csv
import socket               # Import socket module
import time

with open('../data/new.csv') as csvread:
	reader = csv.DictReader(csvread)
	for row in reader:
		uId = row['userId']
		mId = row['movieId']
		mRate = row['rating']
		getStr = 'HTTP GET /item/:'+mId+'/user/:'+uId+'/rat/:'+mRate
		s = socket.socket()         # Create a socket object
		host = 'localhost' 	  # Get local machine name
		port = 8080               # Reserve a port for your service.
		s.connect((host, port))
		s.send(bytearray(getStr,'UTF-8'))
		s.close     		 # Close the socket when done
		time.sleep(0.3)
