"""
Module with Read and Write Connection Pool.
"""


import logging
import time
import typing

from contextlib import contextmanager
from sys import exc_info
from threading import Lock

import psycopg2
# from psycopg2.extensions import STATUS_BEGIN, STATUS_READY

from py_pool_lib.meta_classes import SingletonMeta


logging.basicConfig(level=logging.INFO)


class PoolConn(metaclass=SingletonMeta):

    """
    Pool which is python list and strores DB connections.
    """

    def __init__(self, size: int, *args, **kwargs) -> None:
        """
        Accept db_config as dict in args or as kwargs.
            dbname = the database name (database is a deprecated alias)
            user = user name used to authenticate
            password = password used to authenticate
            host = database host address (defaults to UNIX socket if not provided)
            port = connection port number (defaults to 5432 if not provided)
        """

        self.db_config = (args, kwargs)
        self._pool = []
        self.size = size
        self._lock = Lock()
        self.virgin = True  # Set to False after the pool is used.

    @property
    def db_config(self) -> dict:
        """
        Nicer __init__ with this.
        """

        return {k: v for (k, v) in self._db_config.items() if k !='password'}

    @db_config.setter
    def db_config(self, config_tuple: tuple[tuple[dict], dict]):
        """
        Checks if db_config is given as dict or kwargs.
        """

        if len(config_tuple[0]) != 0:
            self._db_config = config_tuple[0][0]
        else:
            self._db_config = config_tuple[1]

    def _connection(self) -> psycopg2.connect:  # type: ignore
        """
        Create database connection with psycopg2.
        or take it from pool if there is one.
        """

        one_try = 0  # Incremented in the while loop.
        conn = None
        while not conn:
            if len(self._pool) != 0:
                with self._lock:
                    conn = self._pool.pop()
                    logging.info("PULL")
                break
            if one_try:  # Make <if on_try == attempts:> for more attempts
                conn = psycopg2.connect(**self._db_config)
                logging.info("Create connection")
                break
            one_try += 1
            if self.virgin:
                self.virgin = False
                continue
            logging.info("Wait a second.")
            time.sleep(1)
        return conn

    def connection_alive(self, conn: psycopg2.connect):  # type: ignore
        """Checks if connection is alive."""

    def __str__(self):
        db_str = ' '.join(f"{key}={value}" for key, value in
                          self._db_config.items() if key not in ('password', 'user'))

        pool_str = f"Pool of size {self.size} with {len(self._pool)} " + \
                   f"active connections to: {db_str}"

        return pool_str


class PoolReadConn(PoolConn):

    """
    Pool with connections used for reading from DB.
    """

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool."""

        conn = None
        curs = None
        try:
            conn = self._connection()
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            error = f"Problem with transaction: {exc_info()}"
            logging.info(error)
        else:
            logging.info("Data extracted")
        finally:
            if curs:
                curs.close()
            if conn:
                if len(self._pool) < self.size:
                    self._pool.append(conn)
                    logging.info("PUSH")
                else:
                    conn.close()
                    logging.info("Close connection")


class PoolWriteConn(PoolConn):

    """
    Pool with connections used for writing in DB.
    """

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool."""

        conn = None
        curs = None
        try:
            conn = self._connection()
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            error = f"Problem with transaction: {exc_info()}"
            logging.info(error)
            if conn:
                conn.rollback()
        else:
            logging.info("COMMIT")
            conn.commit()
        finally:
            if curs:
                curs.close()
            if conn:
                if len(self._pool) < self.size:
                    self._pool.append(conn)
                    logging.info("PUSH")
                else:
                    conn.close()
                    logging.info("Close connection")
