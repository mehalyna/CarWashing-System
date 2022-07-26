# Task3 - Jordan Petrov
## DB Connection Pool

Generic pooling code for PostgreSQL supporting two types of pools

* Read only
* Read and Write

### Before trying to run this project please run `pip install requirements.txt` 

Connection Pool is nothing but cached database connections created and maintained to get reused for coming requests 
instead of making the new connection every time.

You can specify the number of connections you want to have in a pool

Check /src/python/car_wash/main.py to see how to use a pool as a context manager

Configure your connection data to your db in /src/python/car_wash/config.py

![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
