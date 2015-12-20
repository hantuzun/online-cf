#! /usr/bin/env python3
import redis
import re
import time
#I manually populated r1's list while I ran the script
#Some notes: As queues I used Redis lists and for the 
#adjancency matrix I used redis sets. Since Redis can
#not iterate specific keys r2 must only contain sets
#so that we can represent a matrix structure

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)

members = r1.smembers('user')
item = 'item2'
while len(members) != 0:
	citem = (str(members.pop(), 'utf-8'))
	if citem != item:
		itemUser = item + ':' + citem
		print(itemUser)
		r1.lpush('qiu', itemUser) 
	
	#print(str(members.pop(), 'utf-8'))
