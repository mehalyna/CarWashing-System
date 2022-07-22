import time
from contextlib import contextmanager

import psycopg2

from ..utils import Singleton


DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'db_name': 'carwashDB',
    'username': 'bogdan',
    'password': '123456'
}


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
        while not self._pool:
            time.sleep(1)
        else:
            connection = self._pool.pop()

        yield connection

        self._pool.append(connection)


class RWDBPool(DBPoolBase):

    """Read and write pool of connections."""

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
        while not self._pool:
            time.sleep(1)
        else:
            connection = self._pool.pop()

        yield connection
        connection.commit()

        self._pool.append(connection)


ro_db_pool = RODBPool(
    hostname=DB_CONFIG['host'],
    password=DB_CONFIG['password'],
    username=DB_CONFIG['username'],
    _dbname=DB_CONFIG['db_name'],
    pool_size=3
)

rw_db_pool = RWDBPool(
    hostname=DB_CONFIG['host'],
    password=DB_CONFIG['password'],
    username=DB_CONFIG['username'],
    _dbname=DB_CONFIG['db_name'],
    pool_size=3
)
