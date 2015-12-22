# online-cf
Real-time collaborative filtering for item-item similarities

## Dependencies
```sh
pip3 install redis
```

## Instructions 
Scripts are written in Python 3.
Run the following redis servers running before running the scripts.

```sh
# cd redis.../src

redis-server --port 6379
redis-server --port 6380
redis-server --port 6381
redis-server --port 6382
```

Run the following python scripts in this order:

```sh
# cd online-cf/src 

python3 s1.py
python3 s2.py
python3 s3.py
python3 client.py
```
