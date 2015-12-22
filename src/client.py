#!/usr/bin/python
import csv
import socket

with open('../data/new.csv') as csvread:
    for row in csv.DictReader(csvread):
        requeststr = 'HTTP GET /item/:'+row['movieId']+'/user/:'+row['userId']+'/rat/:'+row['rating']
        print ('requesting ' + requeststr)

        s = socket.socket()
        s.connect(('localhost', 8080))
        s.send(bytearray(requeststr,'UTF-8'))
        s.close

print('Executed all requests.')
