import csv
import random
dictarr = []
with open('small.csv') as csvread:
	reader = csv.DictReader(csvread)
	for row in reader:
		dict = {'userId': row['userId'],'movieId': row['movieId']}
		dictarr.append(dict)
random.shuffle(dictarr)
with open('new.csv', 'w') as csvwrite:
	fieldnames = ['userId', 'movieId']
	writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
	writer.writeheader()
	for element in dictarr:
		writer.writerow(element)




