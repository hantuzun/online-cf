#! /usr/bin/env python3
import redis
import re
import time

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
r2 = redis.StrictRedis(host='localhost', port=6380, db=0)
r3 = redis.StrictRedis(host='localhost', port=6381, db=0)
r4 = redis.StrictRedis(host='localhost', port=6382, db=0)

r1.flushall()
r2.flushall()
r3.flushall()
r4.flushall()
