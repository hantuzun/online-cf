import csv
import random
dictarr = []
with open('../data/small.csv') as csvread:
    reader = csv.DictReader(csvread)
    for row in reader:
        dict = {'userId': row['userId'],'movieId': row['movieId'], 'rating': row['rating']}
        dictarr.append(dict)
random.shuffle(dictarr)
with open('../data/new.csv', 'w') as csvwrite:
    fieldnames = ['userId', 'movieId', 'rating']
    writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
    writer.writeheader()
    for element in dictarr:
        writer.writerow(element)
