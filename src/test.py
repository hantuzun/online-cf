#! /usr/bin/env python3
import csv

#I manually populated r1's list while I ran the script
#Some notes: As queues I used Redis lists and for the 
#adjancency matrix I used redis sets. Since Redis can
#not iterate specific keys r2 must only contain sets
#so that we can represent a matrix structure

ratings = [{'userId': 1, 'movieId': 1, 'rating': 1},
           {'userId': 2, 'movieId': 1, 'rating': 1},
           {'userId': 3, 'movieId': 1, 'rating': 1},
           {'userId': 4, 'movieId': 1, 'rating': 1},
           {'userId': 5, 'movieId': 1, 'rating': 1},
           {'userId': 6, 'movieId': 1, 'rating': 1},
           {'userId': 1, 'movieId': 2, 'rating': 1},
           {'userId': 2, 'movieId': 2, 'rating': 1},
           {'userId': 3, 'movieId': 2, 'rating': 1},
           {'userId': 7, 'movieId': 2, 'rating': 1},
           {'userId': 8, 'movieId': 2, 'rating': 1}]

with open('../data/test.csv', 'w') as csvwrite:
	fieldnames = ['userId', 'movieId', 'rating']
	writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(ratings)

	# for rating in ratings:
	# 	writer.writerow(rating)
