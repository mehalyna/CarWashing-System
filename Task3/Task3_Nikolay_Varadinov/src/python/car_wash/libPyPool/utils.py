"""Module with Connection pools, Connection and Cursor."""

import logging

from threading import Lock
from typing import Type

import psycopg2


logging.basicConfig(level=logging.INFO)


class SingletonMeta(type):

    """Singleton Meta class. After first initialization of an instance
       in its classes, any new changes to __init__ won't have effect on the
       the returned instance.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls.__name__] = instance
        return cls._instances[cls.__name__]


class _Connection:

    """Create connection with custom context manager
     which does not close the connection
     """

    def __init__(self, pool_name: str, config: str) -> None:
        self.pool = pool_name
        self.config = config

    def __enter__(self):
        try:
            conn = psycopg2.connect(self.config)
            return ((self.pool, conn))
        except psycopg2.Error as error:
            logging.info(error.diag.message_primary)
            return ()

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
        pool = SingletonMeta._instances[self.pool_cls_name]
        pool.push((self.pool_cls_name, self.conn))
        logging.info('Connection PUSHED')


class PoolConn(metaclass=SingletonMeta):

    """Pool which is python list and strores DB connections."""

    @staticmethod
    def stringer(db_config: dict) -> str:
        """create string of key word arguments from params_dict"""

        config = (" ").join(
            f"{key}={value}" for key, value in db_config.items())
        return config


    def __init__(self, size: int, *args, **kwargs) -> None:
        if len(args) != 0:
            self.db_config = self.stringer(args[0])
        else:
            self.db_config = self.stringer(kwargs)
        self.pool = []
        self.size = size
        self.name = self.__class__.__name__
        self._lock = Lock()

    def populate_pool(self):
        """Create connections and add to pool"""

        for _ in range(self.size):    # populate pool with connections
            with _Connection(self.name, self.db_config) as conn:
                self.pool.append(conn)

    def pull(self) -> tuple:
        """Pull connection. Using Lock to prevent the race condition"""

        if len(self.pool) == 0:
            print("Pool is empty. Try again later")
            return self.name, None
        with self._lock:
            con_tup = self.pool.pop()
            logging.info('Connection PULLED')
            return con_tup

    def push(self, conn) -> str:
        """Push connection"""

        if len(self.pool) < self.size:
            self.pool.append(conn)
            return "Successfully adding to pool"
        raise Exception("Pool is full. Should not have this connection!")


class PoolReadConn(PoolConn):
    """Pool with connections used for reading from DB"""


class PoolWriteConn(PoolConn):
    """Pool with connections used for writing in DB"""
