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
r2 = redis.StrictRedis(host='localhost', port=6380, db=0)
r3 = redis.StrictRedis(host='localhost', port=6381, db=0)
r4 = redis.StrictRedis(host='localhost', port=6382, db=0)

while True:
	#there must be a list named 'qiu' in r1 first 
	if r1.llen('qiu') != 0:
		pair = str(r1.lpop('qiu'), "utf-8")
		
		#Parse item and user names
		pairReg = re.match(r'(.*):(.*):(.*)', pair, re.M|re.I)

		item = pairReg.group(1)
		user = pairReg.group(2)
		rating = pairReg.group(3)
		if r2.exists(user) != 1:
			r2.incr('userCount')
		#print(item)
		#print(user)
		#test purposesbreak
		#Add 'user' to 'item''s set in r2
		r2.hset(item,user, int(rating))
		r4.sadd(user, int(item))
		#Check in all items for 'user'
		members = r4.smembers(user)
		while len(members) != 0:
			citem = (str(members.pop(), 'utf-8'))
			if citem != item:
				itemUser = item + ':' + citem
				print(itemUser)
				r3.lpush('qii', itemUser)		