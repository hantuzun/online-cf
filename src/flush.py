#! /usr/bin/env python3
import redis

redisports = [6379, 6380, 6381, 6382]

for port in redisports:
    redis.StrictRedis(host='localhost', port=port, db=0).flushall()
