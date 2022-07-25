"""DB pool manager. 
It is module that describes steps to connect to DB.
It uses pool of connection to avoid load on DB side.
"""

import logging
import psycopg2
import time
import typing

from contextlib import contextmanager
from collections import deque
from python.carwash.utils.utils import Singleton
from src.python.carwash.DB_connections.config import DB_CONFIG
from threading import Lock


logging.basicConfig(format = '%(process)d-%(levelname)s-%(message)s')


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
        self._lock = Lock()

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        try:
            con = psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)
            return con
        except psycopg2.OperationalError:
            logging.critical("Errors detected.")
            

    @contextmanager
    def connection(self) -> typing.Generator:
        if not self._pool:
            while not self._pool:
                logging.error("Must wait for free connection")
                time.sleep(1)
        with self._lock: #using lock to prevent race conditions
            connection = self._pool.popleft() #popleft faster than pop
            logging.info("Connection added")
            yield connection
            #add connection to deque
            self._pool.append(connection)
        connection = None
        logging.info("Connection has gone back to the pool.")

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
        try:
            con = psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)
            return con
        except psycopg2.OperationalError:
            logging.critical("Errors detected.")
            

    @contextmanager
    def transaction(self) -> psycopg2.connect:
        # get connection from pool
        if not self._pool:
            while not self._pool: #when there are no available connections in the pool
                logging.critical("Must wait for free connection")
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