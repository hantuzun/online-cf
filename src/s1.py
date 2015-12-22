#!/usr/bin/python
import redis
import socket
import re

r1 = redis.StrictRedis(host='localhost', port=6379, db=0)
s = socket.socket()
s.bind(('localhost', 8080))
s.listen(5)
print('Can receive actions.')

while True:
    conn, addr = s.accept()
    params = re.findall(r'\b\d+\b', str(conn.recv(1024),'UTF-8'))
    item = params[0]
    user = params[1]
    rating = params[2]
    action = item + ':' + user + ':' + rating  # item:user:rating
    print('User', user, 'rated item', item, rating)

    r1.lpush('qiu', action) 
    conn.close()
