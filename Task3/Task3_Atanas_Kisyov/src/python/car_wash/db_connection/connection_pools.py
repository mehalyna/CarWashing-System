"""Read-only and read/write database connection pools definitions"""
from collections import deque
from contextlib import contextmanager
import logging
import time
import typing

import psycopg2

from utils.singleton import Singleton


class PoolBaseClass(metaclass=Singleton):

    """Base class for creating connection pools"""

    def __init__(self, hostname: str, database_name: str,username: str, password: str, pool_size: int) -> None:
        """Initialize pool"""

        self.hostname = hostname
        self.database_name = database_name
        self.username = username
        self.password = password
        self._pool = deque()
        self.pool_size = pool_size
        self._open_connection = None

    @contextmanager
    def connection(self) -> typing.Generator:
        """Get database connection from pool, yield it, and return it to the pool after it's no longer used"""

        # If there are no connections in the pool, wait until one is returned
        while not self._pool:
            logging.error('There are no free connections at the moment. Please wait for free connection...')
            time.sleep(1)

        # Get connection from pool and log it is successful
        self._open_connection = self._pool.popleft()
        logging.info('A free connection is pulled from the pool!')

        yield self._open_connection

        if self.__class__.__name__ == 'ReadWritePool':
            self._open_connection.commit()

        self._pool.append(self._open_connection)
        self._open_connection = None
        logging.info('Connection has been successfuly returned to the pool!')


    def _create_connection(self) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        try:
            connection =  psycopg2.connect(
                dbname=self.database_name,
                host=self.hostname,
                user=self.username, 
                password=self.password,
                )
            logging.info('Connection successful!')
            return connection
        except psycopg2.OperationalError:
            logging.critical('Connection failed! See exception message and try again!')
            raise psycopg2.OperationalError()
    
    def populate_pool(self) -> None:
        """Populate pool with connections"""
        
        for _ in range(self.pool_size):
            connection = self._create_connection()
            self._pool.append(connection)

        log_message = f'{self.pool_size} connections are added to the pool!'
        logging.info(log_message)


class ReadOnlyPool(PoolBaseClass):

    """Read-only connection pool"""
    pass


class ReadWritePool(PoolBaseClass):

    """Read/Write connection pool"""
    pass
