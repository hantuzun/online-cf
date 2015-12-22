#! /usr/bin/env python3
from __future__ import division # for float point division
import redis
import re
import time

r2 = redis.StrictRedis(host='localhost', port=6380, db=0)
r3 = redis.StrictRedis(host='localhost', port=6381, db=0)

while True:
    if r3.llen('qii') != 0:
        pair = r3.lpop('qii').decode('utf-8')
        pairReg = re.match(r'(.*):(.*)', pair, re.M|re.I)
        
        item1 = pairReg.group(1)
        item2 = pairReg.group(2)

        keys1 = r2.hkeys(item1)
        keys2 = r2.hkeys(item2)

        interCount = 0
        unionCount = 0        
        for key in keys1:
            if r2.hexists(item2, key):
                interCount += 1
                unionCount += 1
            else:
                unionCount += 1

        for key in keys2:
            if r2.hexists(item1, key) != 1:
                unionCount += 1

        if unionCount !=0:
            sim = interCount / unionCount
        else:
            sim = 0

        print ('similarity of', item1, 'and', item2, 'is', sim)

        r3.zadd(item1, sim, item2)
        r3.zadd(item2, sim, item1)

        maxSize = 2;

        # Remove least similar items if similar item set size is larger than maxSize
        for item in [item1, item2]:
            size = r3.zcard(item)
            removeCount = size - maxSize
            if removeCount > 0:
                r3.zremrangebyrank(item, 0, removeCount - 1)
    else:
        time.sleep(1)
