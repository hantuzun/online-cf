#!/usr/bin/python
import redis
import socket
import re

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
s = socket.socket()
s.bind(('localhost', 8080))
s.listen(5)
print('Socket is ready.')

while True:
    conn, addr = s.accept()
    params = re.findall(r'\b\d+\b', str(conn.recv(1024),'UTF-8'))
    action = params[0] + ':' + params[1] + ':' + params[2]
    print('Got the following action: ' + action)

    r1.lpush('qiu', action) 
    conn.close()
