# online-cf
Real-time collaborative filtering for item-item similarities

An implementation of the paper [Cloud based real-time collaborative filtering for item-item recommendations](http://dl.acm.org/citation.cfm?id=2577924). 

We also stored which items every user rated and hence improved the performance.

The `cosine` branch has an experimental implementation of similarity calculation using numeric ratings instead of binary data.

## Dependencies
You must have redis.py. Install it with this instruction:
```sh
$ pip3 install redis
```

## Instructions 
Scripts are written in Python 3.

Run the following redis servers running before running the scripts:
```sh
# cd redis.../src

$ redis-server --port 6379
$ redis-server --port 6380
$ redis-server --port 6381
$ redis-server --port 6382
```

Run the following python scripts via `run` script:
```sh
$ chmod +x run
$ ./run
```

Feed the scripts with data:
```sh
$ python3 client.py
```

Monitor the most similar items to an item live with `similars.py` script:
```sh
$ python3 similars.py 1
Showing the most similar items for 1
[['1220', '0.036'], ['315', '0.036'], ['4886', '0.036'], ['780', '0.036'], ['1923', '0.032'], ['586', '0.032'], ['4973', '0.030'], ['1198', '0.021'], ['457', '0.017'], ['296', '0.014']]
.
.
.
```
