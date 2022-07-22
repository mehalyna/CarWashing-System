"""DB pool manager. 
It is module that describes steps to connect to DB.
It uses pool of connection to avoid load on DB side.
"""

import logging
import psycopg2
import time

from carwash.utils import Singleton
from contextlib import contextmanager
from collections import deque


DB_CONFIG = {'hostname': 'localhost',
            'password': 'root',
            'username': 'postgres',
            'dbname' : 'db',
            'port': 5432} 


class DBPoolBase(metaclass=Singleton):

    """Base class of DB pool."""

    def _create_connection(self) -> psycopg2.connect:
        """Create connection and add it to the pool"""
        raise NotImplementedError('Method is not implemented') #since doesnt return connection
    
    
class ReadOnlyDBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(self, hostname: str, password: str, username: str, _dbname: str, pool_size: int) -> None:
        """Constructor of RODBPool connections 
        
        Parameters:
            - 'hostname' - db hostname
            - 'password' - Password to enter db
            - 'username' - Username to enter db
            - 'dbname' - Name of db
            - 'pool_size' - Amount of connections in the pool
        """
        
        super().__init__()
        self._pool = deque()
        self._hostname = hostname
        self._password = password
        self._username = username
        self._dbname = _dbname
        self._pool_size = pool_size

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        con = psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)
        return con

    @contextmanager
    def connection(self) -> psycopg2.connect:
        if not self._pool:
            while not self._pool:
                logging.error("Must wait for free connection")
                time.sleep(1)

        connection = self._pool.popleft() #popleft faster than pop
        logging.info("Connection added")
        yield connection
        #add connection to deque
        self._pool.append(connection)

class ReadWriteDBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(self, hostname: str, password: str, username: str, _dbname: str, pool_size: int) -> None:
        """Constructor of RODBPool connections
        
        Parameters:
            - 'hostname' - db hostname
            - 'password' - Password to enter db
            - 'username' - Username to enter db
            - 'dbname' - Name of db
            - 'pool_size' - Amount of connections in the pool
        """

        super().__init__()
        self._pool = deque()
        self._hostname = hostname
        self._password = password
        self._username = username
        self._dbname = _dbname
        self._pool_size = pool_size

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        con = psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)
        return con

    @contextmanager
    def transaction(self) -> psycopg2.connect:
        # get connection from pool
        if not self._pool:
            while not self._pool: #when there are no available connections in the pool
                logging.error("Must wait for free connection")
                time.sleep(1)

        connection = self._pool.popleft() #popleft faster than pop
        logging.info("Connection added")
        yield connection

        connection.commit()
        self._pool.append(connection) # add to deque

        

# Initialization of Read Write pool object
rw_db_pool = ReadWriteDBPool(DB_CONFIG['hostname'], DB_CONFIG['password'], DB_CONFIG['username'], DB_CONFIG['dbname'], pool_size = 3)
    

# Initialization of Read Only pool object
ro_db_pool = ReadOnlyDBPool(DB_CONFIG['hostname'], DB_CONFIG['password'], DB_CONFIG['username'], DB_CONFIG['dbname'], pool_size = 3)