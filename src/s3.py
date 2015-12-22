#! /usr/bin/env python3
import redis
import re
import time
import math as m

#r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
r2 = redis.StrictRedis(host='localhost', port=6380, db=0)
r3 = redis.StrictRedis(host='localhost', port=6381, db=0)

while True:
    if r3.llen('qii') != 0:
        pair = str(r3.lpop('qii'), "utf-8")
        pairReg = re.match(r'(.*):(.*)', pair, re.M|re.I)
        
        item1 = pairReg.group(1)
        item2 = pairReg.group(2)

        numerator = 0
        denom1 = 0
        denom2 = 0
        
        keys1 = r2.hkeys(item1)
        keys2 = r2.hkeys(item2)
        unionCount = 0
        for key in keys1:
            denom1 += int(str(r2.hget(item1, key), 'utf-8'))**2
            if r2.hexists(item2, key):
                numerator += int(str(r2.hget(item1, key), 'utf-8'))*int(str(r2.hget(item2, key),'utf-8'))
                unionCount += 1
            else:
                numerator += int(str(r2.hget(item1, key), 'utf-8'))*3
                unionCount += 1
        for key in keys2:
            denom2 += int(str(r2.hget(item2, key), 'utf-8'))**2
            if r2.hexists(item1,key) != 1:
                numerator += int(str(r2.hget(item2, key),'utf-8'))*3
                unionCount += 1
        missingCount1 = int(str(r2.get('userCount'),'utf-8')) - r2.hlen(item1)
        missingCount2 = int(str(r2.get('userCount'), 'utf-8')) - r2.hlen(item2)

        denom1 += missingCount1 * 9
        denom2 += missingCount2 * 9
        denom1 = m.sqrt(denom1)
        denom2 = m.sqrt(denom2)

        denom = denom1 * denom2

        sim = numerator / denom

        r3.zadd(item1, item2, sim)
        r3.zadd(item2, item1, sim)
