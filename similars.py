#! /usr/bin/env python3
import redis
import sys
import time

item = 1;
if len(sys.argv) == 2:
    item = sys.argv[1];

print('Showing the most similar items for', item)

r3 = redis.StrictRedis(host='localhost', port=6381, db=0)

while True:
    similars = r3.zrange(item, 0, -1, desc=True, withscores=True)
    print (similars)
    time.sleep(1)
