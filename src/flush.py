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

r1.flushall()
r2.flushall()
r3.flushall()
r4.flushall()
