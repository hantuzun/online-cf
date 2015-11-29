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

while True:
	#there must be a list named 'qiu' in r1 first 
	if r1.llen('qiu') != 0:
		pair = str(r1.lpop('qiu'), "utf-8")
		
		#Parse item and user names
		pairReg = re.match(r'(.*):(.*)', pair, re.M|re.I)

		item = pairReg.group(1)
		user = pairReg.group(2)
		#print(item)
		#print(user)
		#test purposesbreak
		#Add 'user' to 'item''s set in r2
		r2.sadd(item,user)
		#Check in all items for 'user'
		for item2 in r2.scan_iter():
			if(str(item2, "utf-8") != item):
				#print('key')
				#print(str(key, "utf-8"))

				#If 'user' is a member of 'item2's user set
				#push item:item2 into r3's queue
				if(r2.sismember(str(item2, "utf-8"), user) == 1):
					itemitem = item + ':' + str(item2, "utf-8")
					
					r3.lpush('qii', itemitem)
					#test purposes r3.lrange('qii', 0, -1)
				#test purposes time.sleep(2)
		