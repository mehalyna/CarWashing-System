import logging
import time
from contextlib import contextmanager
from threading import Lock

import psycopg2

from utils.singleton import Singleton
from utils.user import READ_ONLY_USER, READ_WRITE_USER


class DBPoolBase(metaclass=Singleton):

    """Base class of DB pool."""

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        raise NotImplementedError("No code added into _create_connection method")

    def _get_connection(self) -> psycopg2.connect:
        """Get connection from pool"""
        raise NotImplementedError("No code added into _get_connection method")

    def _put_connection(self, conn: psycopg2.connect) -> None:
        """Put connection back to pool"""
        raise NotImplementedError("No code added into _put_connection method")


class RODBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(
        self, hostname: str, password: str, username: str, _dbname: str, pool_size: int
    ) -> None:
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
        self._lock = Lock()

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        return psycopg2.connect(
            dbname=self._dbname,
            user=self._username,
            password=self._password,
            host=self._hostname,
        )

    def _get_connection(self) -> psycopg2.connect:
        """Get connection from pool"""

        while True:
            with self._lock:
                if len(self._pool) > 0:
                    return self._pool.pop()
                else:
                    time.sleep(1)

    def _put_connection(self, conn: psycopg2.connect) -> None:
        """Put connection back to pool"""
        with self._lock:
            self._pool.append(conn)

    @contextmanager
    def connection(self):
        """
        Context manager for the read only pool.
        Use cursor to execute queries.
        """
        if len(self._pool) < self._pool_size:
            self._pool.append(self._create_connection())

        conn = self._get_connection()
        cursor_ = conn.cursor()
        try:
            yield cursor_
        except psycopg2.Error:
            logging.error("Invalid query.")
            raise psycopg2.Error("Invalid query.")
        finally:
            self._put_connection(conn)


class RWDBPool(DBPoolBase):

    """Read only pool of connections."""

    def __init__(
        self, hostname: str, password: str, username: str, _dbname: str, pool_size: int
    ) -> None:
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
        self._lock = Lock()

    def _create_connection(self) -> psycopg2.connect:
        """Create connection to DB"""
        return psycopg2.connect(
            dbname=self._dbname,
            user=self._username,
            password=self._password,
            host=self._hostname,
        )

    def _get_connection(self) -> psycopg2.connect:
        """Get connection from pool"""

        while True:
            with self._lock:
                if len(self._pool) > 0:
                    return self._pool.pop()
                else:
                    time.sleep(1)

    def _put_connection(self, conn: psycopg2.connect) -> None:
        """Put connection back to pool"""
        with self._lock:
            self._pool.append(conn)

    @contextmanager
    def transaction(self):
        """
        Context manager for the read write pool.
        Use cursor to execute queries.
        """

        if len(self._pool) < self._pool_size:
            self._pool.append(self._create_connection())

        conn = self._get_connection()
        cursor_ = conn.cursor()
        try:
            yield cursor_
        except psycopg2.Error:
            logging.error("Invalid query.")
            raise psycopg2.Error("Invalid query.")
        finally:
            conn.commit()
            cursor_.close()
            self._put_connection(conn)


# Initialization of RO pool object
ro_pool = RODBPool(**READ_ONLY_USER)
# Initialization of RW pool object
rw_pool = RWDBPool(**READ_WRITE_USER)
