#! /usr/bin/env python3
import redis
import re
import time
import csv

dictarr = []
#I manually populated r1's list while I ran the script
#Some notes: As queues I used Redis lists and for the 
#adjancency matrix I used redis sets. Since Redis can
#not iterate specific keys r2 must only contain sets
#so that we can represent a matrix structure
dict = {'userId': 1,'movieId': 1, 'rating': 1}
dictarr.append(dict)
dict2 = {'userId': 2,'movieId': 1, 'rating': 1}
dictarr.append(dict2)
dict3 = {'userId': 3,'movieId': 1, 'rating': 1}
dictarr.append(dict3)
dict4= {'userId': 4,'movieId': 1, 'rating': 1}
dictarr.append(dict4)
dict5 = {'userId': 5,'movieId': 1, 'rating': 1}
dictarr.append(dict5)
dict6 = {'userId': 6,'movieId': 1, 'rating': 1}
dictarr.append(dict6)
dict7 = {'userId': 1,'movieId': 2, 'rating': 1}
dictarr.append(dict7)
dict8 = {'userId': 2,'movieId': 2, 'rating': 1}
dictarr.append(dict8)
dict9 = {'userId': 3,'movieId': 2, 'rating': 1}
dictarr.append(dict9)
dict10 = {'userId': 7,'movieId': 2, 'rating': 1}
dictarr.append(dict10)
dict11 = {'userId': 8,'movieId': 2, 'rating': 1}
dictarr.append(dict11)



with open('../data/test.csv', 'w') as csvwrite:
	fieldnames = ['userId', 'movieId', 'rating']
	writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
	writer.writeheader()
	for element in dictarr:
		writer.writerow(element)

