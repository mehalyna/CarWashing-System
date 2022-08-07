import psycopg2
import logging

from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from src.python.car_wash.utils import Singleton

DSN = 'postgresql://postgres:password@localhost/carwash?connect_timeout=1'

DB_CONFIG = {
    'hostname': 'localhost',
    'port': '5432',
    'dbname': 'carwash',
    'username': 'postgres',
    'password': 'postgres'
}


class DBHelper(metaclass=Singleton):
    """Base class of DB pool."""

    def __init__(self, conns: int, *args, **kwargs) -> None:
        self._pool = []
        self.conns = int(conns)
        self._kwargs = kwargs
        self._args = args
        self._connection_pool = None

    def initialize_connection_pool(self) -> psycopg2.connect:
        """Create a new connection"""

        db_dsn = DSN
        self._connection_pool = pool.SimpleConnectionPool(1, 5, db_dsn)
        logging.info('Pool initialized.')

    def shutdown_connection_pool(self) -> None:
        """
        Close cursor, commit connection and returns the connection to the pool.
        """
        if self._connection_pool is not None:
            self._connection_pool.closeall()
            logging.info('Pool closed.')


class RWDBPool(DBHelper):
    """Pool for read and write db users"""

    @contextmanager
    def rw_pool(self, autocommit=True):
        """
        Context manager for the read and write pool.
        Use cursor to execute queries.
        """
        if self._connection_pool is None:
            self.initialize_connection_pool()
        conn = self._connection_pool.getconn()
        conn.autocommit = autocommit
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        logging.info('Read and write user logged.')

        try:
            yield cursor, conn

        finally:
            cursor.close()
            self._connection_pool.putconn(conn)


class RODBPool(DBHelper):
    """Pool for read only db users"""

    @contextmanager
    def ro_pool(self):
        """
        Context manager for the read only pool.
        Use cursor to execute queries.
        """

        if len(self._pool) < self.conns:
            self._pool.append(self.initialize_connection_pool())
        conn = self.initialize_connection_pool()
        cursor = conn.cursor()
        try:
            yield cursor
        except psycopg2.Error:
            logging.error("Invalid query.")
            raise psycopg2.Error("Invalid query.")
        finally:
            self.shutdown_connection_pool(conn)


rw_pool_helper = RWDBPool(3,
                          hostname=DB_CONFIG['hostname'],
                          password=DB_CONFIG['password'],
                          username=DB_CONFIG['username'],
                          _dbname=DB_CONFIG['dbname'],
                          )

ro_pool_helper = RODBPool(3,
                          hostname=DB_CONFIG['hostname'],
                          password=DB_CONFIG['password'],
                          username=DB_CONFIG['username'],
                          _dbname=DB_CONFIG['dbname'],
                          )
