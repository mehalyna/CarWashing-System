"""DB pool manager. 
It is module that describes steps to connect to DB.
It uses pool of connection to avoid load on DB side.
"""

import logging
from contextlib import contextmanager

import psycopg2

from utils import Singleton



DB_CONFIG = {'hostname': 'localhost'} # all other DB params should be here


class DBPoolBase(metaclass=Singleton):

    """Base class of DB pool."""
    
    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        raise NotImplementedError('No code added into _create_connection method')


class RODBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(self, hostname: str, password: str, username: str, _dbname: str, pool_size: int) -> None:
        """Constructor of RODBPool connections
        
        :Parameters:
            - `hostname` - DB hostname
        """
        super().__init__()
        self._pool = []
        self._hostname = hostname
        self._password = password
        self._username = username
        self._dbname = _dbname
        self._pool_size = pool_size

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        return psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)

    @contextmanager
    def connection(self) -> psycopg2.connect:
         # get connection from pool
        yield connection()
        ....
        # return connection into poll


class RWDBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(self, hostname: str, password: str, username: str, _dbname: str, pool_size: int) -> None:
        """Constructor of RODBPool connections
        
        :Parameters:
            - `hostname` - DB hostname
        """
        super().__init__()
        self._pool = []
        self._hostname = hostname
        self._password = password
        self._username = username
        self._dbname = _dbname
        self._pool_size = pool_size

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        return psycopg2.connect(dbname=self._dbname,
                                user=self._username,
                                password=self._password,
                                host=self._hostname)

    @contextmanager
    def transaction(self) -> psycopg2.connect:
        # get connection from pool
        yield connection
        connection.commit()
        ....
        # return connection into poll

# Initialization of RO pool object
ro_db_pool = RODBPool()
