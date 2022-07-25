"""Module with Read and Write Connection Pool."""


import logging
import time
import typing

from contextlib import contextmanager
from sys import exc_info
from threading import Lock

import psycopg2

from . meta_classes import SingletonMeta


logging.basicConfig(level=logging.INFO)


class PoolConn(metaclass=SingletonMeta):

    """Pool which is python list and strores DB connections."""

    def __init__(self, size: int, *args, **kwargs) -> None:
        """Accept db_config as dict in args or as kwargs."""

        self.db_config = (args, kwargs)
        self.pool = []
        self.size = size
        self._lock = Lock()
        self.virgin = True

    @property
    def db_config(self) -> dict:
        """Nicer __init__ with this."""

        return self._db_config

    @db_config.setter
    def db_config(self, config_tuple: tuple[tuple[dict], dict]):
        """Checks if db_config is given as dict or kwargs."""

        if len(config_tuple[0]) != 0:
            self._db_config = config_tuple[0][0]
        else:
            self._db_config = config_tuple[1]

    def _connection(self) -> psycopg2.connect: #type: ignore
        """Create database connection with psycopg2.
        or take it from pool if there is one. """

        one_try = 0
        conn = None
        while not conn:
            if len(self.pool) != 0:
                with self._lock:
                    conn = self.pool.pop()
                    logging.info("PULL")
                break
            if one_try:
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

class PoolReadConn(PoolConn):

    """Pool with connections used for reading from DB"""

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool"""

        try:
            conn = self._connection()
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            error = f"Problem with transaction {exc_info()}"
            logging.info(error)
        else:
            logging.info("READ")
            curs.close()
            if len(self.pool) < self.size:
                self.pool.append(conn)
                logging.info("PUSH")
            else:
                conn.close()
                logging.info("Close connection")

class PoolWriteConn(PoolConn):

    """Pool with connections used for writing in DB"""

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool"""

        try:
            conn = self._connection()
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            error = f"Problem with transaction {exc_info()}"
            logging.info(error)
        else:
            logging.info("COMMIT")
            conn.commit()
            curs.close()
            if len(self.pool) < self.size:
                self.pool.append(conn)
                logging.info("PUSH")
            else:
                conn.close()
                logging.info("Close connection")
