# online-cf
Real-time collaborative filtering for item-item similarities

## Dependencies
```sh
pip3 install redis
```

## Instructions 
Scripts are written in Python 3.
Have your redis servers running before running the scripts.

```sh
# cd redis

make
src/redis-server --port 6379
```

Run the following python scripts at the same time:

```sh
# cd online-cf/src 

python3 s1.py
python3 client.py
python3 s2.py
python3 s3-jacc.py
```
