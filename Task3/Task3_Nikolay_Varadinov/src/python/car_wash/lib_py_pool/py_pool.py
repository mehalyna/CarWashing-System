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

    @staticmethod
    def stringer(db_config: dict) -> str:
        """Create string of key word arguments from dict."""

        config = (" ").join(
            f"{key}={value}" for key, value in db_config.items())
        return config

    def __init__(self, size: int, *args, **kwargs) -> None:
        """Accept db_config as dict in args or as kwargs."""

        self.db_config = (args, kwargs)
        self.pool = []
        self.size = size
        self._lock = Lock()
        self._populate_pool()

    @property
    def db_config(self):
        """Nicer __init__ with this."""

        return self._db_config

    @db_config.setter
    def db_config(self, config_tuple: tuple[tuple[dict], dict]):
        """Checks if db_config is given as dict or kwargs."""

        if len(config_tuple[0]) != 0:
            self._db_config = self.stringer(config_tuple[0][0])
        else:
            self._db_config = self.stringer(config_tuple[1])

    def _create_connection(self) -> psycopg2.connect:  # type: ignore
        """Create database connection with psycopg2."""

        return psycopg2.connect(self.db_config)

    def _pull(self) -> psycopg2.connect:  # type: ignore
        """Pull connection. Using Lock to prevent the race conditions."""

        with self._lock:
            while len(self.pool) == 0:
                logging.info("No connection available. Wait a second.")
                time.sleep(1)
            conn = self.pool.pop()
            logging.info("Connection PULLED")
            return conn


    def _push(self, conn) -> None:
        """Push connection to pool."""

        if len(self.pool) < self.size:
            self.pool.append(conn)
            logging.info("Connection PUSHED")
        if len(self.pool) > self.size:
            raise Exception("Pool is full. Should not have this connection!")

    def _populate_pool(self) -> None:
        """Create connections and add to pool."""

        for _ in range(self.size):
            try:
                conn = self._create_connection()
                logging.info("Create connection")
                self._push(conn)
            except psycopg2.Error:
                print("DB Error")
        logging.info("%s populated with %d connections",
                     self.__class__.__name__, self.size)


class PoolReadConn(PoolConn):

    """Pool with connections used for reading from DB"""

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool"""


        conn = self._pull()
        try:
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            print(f"Problem with transaction {exc_info()}")
        except IndexError:
            print("Try again later.")
        else:
            curs.close()
            logging.info("Read from DB")
        finally:
            try:
                conn.isolation_level
            except psycopg2.OperationalError:
                print("Connection dead")
                conn = self._create_connection
            self._push(conn)



class PoolWriteConn(PoolConn):

    """Pool with connections used for writing in DB"""

    @contextmanager
    def transaction(self) -> typing.Generator:
        """Pull connection, and after use return it to pool"""

        conn = self._pull()
        try:
            curs = conn.cursor()
            yield curs
        except psycopg2.Error:
            print(f"Problem with transaction {exc_info()}")
        except IndexError:
            print("Try again later.")
        else:
            conn.commit()
            curs.close()
            logging.info('Commit to DB')
        finally:
            try:
                conn.isolation_level
            except psycopg2.OperationalError:
                print("Connection dead")
                conn = self._create_connection
            self._push(conn)
