# online-cf
Real-time collaborative filtering for item-item similarities

## Dependencies
```sh
pip3 install redis
```

## Instructions 
Scripts are written in Python 3.
Have your redis servers running before running the scripts.


## Latest Issues

 - Not sure about the cosine similarity calculation. it needs testing with a smaller and more controllable dataset.

 - You must install and configure redis on your locals. Feel free with changing the ports on each script.

 - The test run is like this: fire up s1.py, client.py, s2.py and s3.py in order for best tests.

 - s2.py fails at some point because of something related with redis functions sadd and hset (I think it's a minor issue).
