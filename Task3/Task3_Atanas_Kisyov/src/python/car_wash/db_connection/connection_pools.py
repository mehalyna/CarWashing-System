"""Read-only and read/write database connection pools definitions"""
from collections import deque
import logging
import time

import psycopg2

from python.car_wash.db_connection.pool_base_class import PoolBaseClass


class ReadOnlyPool(PoolBaseClass):

    """Read-only connection pool"""

    def __init__(self, hostname, database_name, pool_size: int) -> None:
        """Initialize read-only pool"""

        self.hostname = hostname
        self.database_name = database_name
        self._pool = deque()
        self.pool_size = pool_size
        self._open_connection = None
    
    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""

        if not self._pool:
            
            # If there are no connections in the pool, wait until one is returned
            while not self._pool:
                logging.error('There are no free connections at the moment. Please wait for free connection...')
                time.sleep(1)

        self._open_connection = self._pool.popleft()
        logging.info('A free connection is pulled from the pool!')
        yield self._open_connection

    def __exit__(self) -> None:
        """Return database connection to the pool"""

        self._pool.append(self._current_connection)
        self._open_connection = None
        logging.info('Connection has been successfuly returned to the pool!')
    
    def _create_connection(self, username: str, password: str) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        try:
            connection =  psycopg2.connect(
                dbname=self.database_name,
                hostname=self.hostname,
                user=username, 
                password=password,
                )
            logging.info('Connection successful!')
            return connection
        except psycopg2.OperationalError:
            logging.critical('Connection failed! See exception message and try again!')
            raise psycopg2.OperationalError()
    
    def populate_pool(self, credentials: list) -> None:
        """Populate pool with read-only connections"""
        
        # Limit pool size to the desired length 
        # Raise exception if the desired number of connections is higher than the available credentials
        if len(credentials) >= self.pool_size:
            credentials = credentials[:self.pool_size]
        else:
            raise ValueError(f'Not enough connection credentials. Maximum number of connections is {len(credentials)}')

        for user_credentials in credentials:
            connection = self._create_connection(*user_credentials)
            self._pool.append(connection)

        log_message = f'{self.pool_size} connections are added to the pool!'
        logging.info(log_message)


class ReadWritePool(ReadOnlyPool):

    """Read/Write connection pool"""

    def __init__(self, pool_size: int) -> None:
        """Initialize read/write pool"""
        super().__init__(pool_size)
    
    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""
        return super().__enter__()
    
    def __exit__(self) -> None:
        """Return database connection to the pool"""
        return super().__exit__()
    
    def _create_connection(self, credentials: list) -> psycopg2.connect:
        """Create connection and add it to the pool"""
        return super()._create_connection()
    
    def populate_pool(self, credentials: list) -> None:
        """Populate pool with read/write connections"""
        return super().populate_pool(credentials)
