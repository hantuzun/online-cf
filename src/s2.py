#! /usr/bin/env python3
import redis
import re

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
r2 = redis.StrictRedis(host='localhost', port=6380, db=0)
r3 = redis.StrictRedis(host='localhost', port=6381, db=0)
r4 = redis.StrictRedis(host='localhost', port=6382, db=0)

while True:
	#There must be a list named 'qiu' in r1 first 
	if r1.llen('qiu') != 0:
		pair = r1.lpop('qiu').decode("utf-8")

		# Parse item and user names
		# item:user:rating
		pairReg = re.match(r'(.*):(.*):(.*)', pair, re.M|re.I)

		item = pairReg.group(1)
		user = pairReg.group(2)
		rating = pairReg.group(3)

		# Add the user to item's set in r2
		r2.hset(item, user, rating)
		
		# Add the item to user's set in r4
		r4.sadd(user, item)

		# Put all item:alsowatcheditem pairs to qii
		commonItems = r4.smembers(user)
		while len(commonItems) != 0:
			commonItem = commonItems.pop().decode("utf-8")
			if commonItem != item:
				itemPair = item + ':' + commonItem
				print(itemPair)
				r3.lpush('qii', itemPair)