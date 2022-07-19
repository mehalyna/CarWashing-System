"""Module with Connection pools, Connection and Cursor."""

import logging

from threading import Lock
from typing import Type

import psycopg2


logging.basicConfig(level=logging.INFO)


class SingletonMeta(type):

    """Singleton Meta class. It's classes will run __init__ only once"""

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection:

    """Create connection with custom context manager
     which does not close the connection
     """

    def __init__(self, pool: str, conn_params=None, **kwargs) -> None:
        self.pool = pool
        if conn_params:
            self.params = conn_params
        else:
            self.params = (" ").join(
                f"{key}={value}" for key, value in kwargs.items())

    def __enter__(self):
        try:
            conn = psycopg2.connect(self.params)
            return (self.pool, conn)
        except psycopg2.Error as error:
            logging.info(error.diag.message_primary)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            logging.info(exc_tb)
        else:
            logging.info('Connection CREATED')


class Cursor:

    """Create cursor with custom context manager"""

    def __init__(self, conn: tuple) -> None:
        self.conn = conn[1]
        self.pool_cls_name = conn[0]
        self.currs: Type

    def __enter__(self):
        self.currs = self.conn.cursor()
        logging.info('CURSOR CREATED')
        return self.currs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.currs.close()
        self.conn.commit()
        if self.pool_cls_name == PoolReadConn.__name__:  # Use the singleton to take the pool
            ro_pool = PoolReadConn()
            ro_pool.push((self.pool_cls_name, self.conn))
        else:
            rw_pool = PoolWriteConn()
            rw_pool.push((self.pool_cls_name, self.conn))
        logging.info('Connection PUSHED')


class PoolConn(metaclass=SingletonMeta):

    """Pool which is python list and strores DB connections."""

    def __init__(self, size: int = 3) -> None:
        """Pool and its size"""
        self.pool = []
        self.size = size
        self._lock = Lock()

    def pull(self) -> Connection:
        """Pull connection. Using Lock to prevent the race condition"""

        with self._lock:
            if len(self.pool) >= 1:
                logging.info('Connection PULLED')
                return self.pool.pop()

        raise Exception("No connecton available")

    def push(self, conn: tuple) -> str:
        """Push connection"""

        if len(self.pool) < self.size:
            self.pool.append((conn))
            return "Successfully adding to pool"
        raise Exception("Pool is full. Should not have this connection!")


class PoolReadConn(PoolConn):
    """Pool with connections used for reading from DB"""


class PoolWriteConn(PoolConn):
    """Pool with connections used for writing in DB"""


def create_pools(size_ro: int = 3, size_rw: int = 3) -> dict:
    """Create read and write connection pools and returns
    their instances in a dictionary with keys 'ro' and 'rw'
    """

    ro_pool = PoolReadConn(size_ro)
    rw_pool = PoolWriteConn(size_rw)
    logging.info('Pools CREATED')

    return {'ro': ro_pool, 'rw': rw_pool}
