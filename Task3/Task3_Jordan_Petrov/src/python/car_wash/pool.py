"""
Generic db pooling code for two types of db users:
 - read and write,
 - read only
You can use them as context manager
You can run 'python3 pool.py -h' see how to parse parameters from console
"""
import logging
import time
from contextlib import contextmanager
from threading import Lock

import psycopg2

from config import READ_ONLY_USER, READ_WRITE_USER
from utils import SingletonMeta


class BaseConnectionPool(metaclass=SingletonMeta):

    """
    Base class for the read only and read write classes
    """

    def __init__(self, conns: int, host: str, port: int, user: str, password: str, dbname: str):
        """
        Class constructor
        param conns: number of open connections
        all parameters bellow are passed to psycopg2.connect() method
        param host: host address of db
        param port: port of db
        param user: user of db
        param: password: password of user
        param: dbname: name of db
        """
        self._dbname = dbname
        self._password = password
        self._user = user
        self._port = port
        self._host = host
        self._conns = int(conns)
        self._pool: list[psycopg2.connect] = []
        self._lock = Lock()

    def _connect(self) -> psycopg2.connect:
        """Create a new connection"""

        try:
            conn = psycopg2.connect(
                host=self._host,
                port=self._port,
                user=self._user,
                password=self._password,
                dbname=self._dbname,
            )
        except psycopg2.Error:
            logging.error('Invalid connection parameters.')
            raise psycopg2.Error('Invalid connection parameters.')
        self._pool.append(conn)
        return conn

    def _get_connection(self) -> psycopg2.connect:
        """Get a connection from pool"""

        while not self._pool:
            time.sleep(1)

        with self._lock:
            if self._pool:
                logging.info('Connection has been pulled')
                return self._pool.pop()
        logging.error('No connections available.')
        raise Exception('No connections available.')

    def _put_connection(self, conn: psycopg2.connect):
        """
        Return connection to the pool
        param conn: specified connection to return to the pool.
        """

        if len(self._pool) < self._conns:
            self._pool.append(conn)
            logging.info('Connection returned to the pool.')
        else:
            logging.error('Connection cannot be returned.')


class RWPool(BaseConnectionPool):

    """Pool for read and write db users"""

    @contextmanager
    def transaction(self):
        """
        Context manager for the read write pool.
        Use cursor to execute queries.
        """
        conn = self._get_connection()
        cursor_ = conn.cursor()
        try:
            yield cursor_
        except psycopg2.Error:
            logging.error('Invalid query.')
            raise psycopg2.Error('Invalid query.')
        finally:
            conn.commit()
            cursor_.close()
            self._put_connection(conn)


class ROPool(BaseConnectionPool):

    """Pool for read only db users"""

    @contextmanager
    def connection(self):
        """
        Context manager for the read only pool.
        Use cursor to execute queries.
        """
        conn = self._get_connection()
        cursor_ = conn.cursor()
        try:
            yield cursor_
        except psycopg2.Error:
            logging.error('Invalid query.')
            raise psycopg2.Error('Invalid query.')
        finally:
            self._put_connection(conn)


read_only = ROPool(**READ_ONLY_USER)
read_write = RWPool(**READ_WRITE_USER)
