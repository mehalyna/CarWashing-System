"""Read-only and read/write database connection pools definitions"""
import logging
import time
import typing
from collections import deque
from contextlib import contextmanager
from threading import Lock

import psycopg2

from utils.singleton import Singleton


class PoolBaseClass:

    """Base class for creating connection pools"""

    def __init__(self, # pylint: disable=too-many-arguments
                hostname: str,
                database_name: str,
                username: str,
                password: str,
                pool_size: int=2,
                ) -> None:
        """Initialize pool"""

        self.hostname = hostname
        self.database_name = database_name
        self.username = username
        self.password = password
        self.pool_size = pool_size
        self._pool = deque()
        self._lock = Lock()

    def create_connection(self) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        try:
            connection =  psycopg2.connect(
                dbname=self.database_name,
                host=self.hostname,
                user=self.username,
                password=self.password,
                )
            logging.info('Connection successful!')
            self.pool_size -= 1
            return connection
        except psycopg2.OperationalError as exception:
            logging.critical('Connection failed! \
                See exception message and try again!')
            raise psycopg2.OperationalError(exception)

    def get_connection(self) -> psycopg2.connect:
        """Get connection from the pool"""

        connection = None

        while not connection:
            with self._lock:

                if self.pool_size > 0:
                    connection = self.create_connection()
                    continue

                if self._pool:
                    connection = self._pool.popleft()
                    continue

                logging.error('There are no free connections, please wait!')
                time.sleep(0.1)
        
        return connection

    def return_connection(self, connection: psycopg2.connect) -> None:
        """Return connection to the pool"""

        self._pool.append(connection)
        logging.info('Connection has been successfully returned to the pool!')


class ReadOnlyPool(PoolBaseClass, metaclass=Singleton):

    """Read-only connection pool"""

    @contextmanager
    def connection(self) -> typing.Generator:
        """
        Get database connection from pool, yield it, and
        return it to the pool after it's no longer used
        """

        open_connection = self.get_connection()
        try:
            yield open_connection
        finally:
            self.return_connection(open_connection)


class ReadWritePool(PoolBaseClass, metaclass=Singleton):

    """Read/Write connection pool"""

    @contextmanager
    def connection(self) -> typing.Generator:
        """
        Get database connection from pool, yield it,
        commit and return it to the pool after it's no longer used
        """

        open_connection = self.get_connection()
        try:
            yield open_connection
        finally:
            open_connection.commit()
            self.return_connection(open_connection)
