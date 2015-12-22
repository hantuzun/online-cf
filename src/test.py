#! /usr/bin/env python3
import csv

actions = [{'userId': 1, 'movieId': 1, 'rating': 1},
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
    writer.writerows(actions)
