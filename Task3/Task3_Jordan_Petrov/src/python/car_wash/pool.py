"""
Generic db pooling code for two types of db users:
 - read and write,
 - read only
You can use them as context manager
You can run 'python3 pool.py -h' see how to parse parameters from console
"""
import argparse
import logging

import psycopg2

from config import READ_ONLY_USER, READ_WRITE_USER
from utils import SingletonMeta

logging.basicConfig(
    filename='../../../pool.log',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)


class BaseConnectionPool(metaclass=SingletonMeta):
    """
    Base class for the read only and read write classes
    """

    def __init__(self, conns: int, *args, **kwargs):
        """
        Class constructor
        param conns: number of open connections
        param args: passed to psycopg2.connect
        param kwargs: passed to psycopg2.connect
        """
        self._kwargs = kwargs
        self._args = args
        self.conns = int(conns)
        self._pool: list[psycopg2.connect] = []

        for _ in range(self.conns):
            self._connect()
        logging.info(f'Connection to db established, added needed connections to the pool.')

    def __enter__(self):
        """
        Allows to use the connection pool as a context manager.
        Use cursor to execute queries.
        """
        self.connection = self._get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close cursor, commit connection and returns the connection to the pool.
        """
        self.connection.commit()
        self.cursor.close()
        self._put_connection(self.connection)

    def _connect(self) -> psycopg2.connect:
        """Create a new connection"""
        try:
            conn = psycopg2.connect(*self._args, **self._kwargs)
        except psycopg2.Error:
            logging.error('Invalid connection parameters.')
            raise psycopg2.Error('Invalid connection parameters.')
        self._pool.append(conn)
        return conn

    def _get_connection(self) -> psycopg2.connect:
        """Get a connection from pool"""
        if self._pool:
            logging.info('Connection has been pooled out.')
            return self._pool.pop()
        logging.warning('No available connections.')
        return 'No free connections'

    def _put_connection(self, conn: psycopg2.connect):
        """
        Return connection to the pool
        param conn: specified connection to return to the pool.
        """

        if len(self._pool) < self.conns:
            self._pool.append(conn)
            logging.info('Connection returned to the pool.')
        else:
            logging.error('Connection cannot be returned.')


class RWPool(BaseConnectionPool):
    """Pool for read and write db users"""


class ROPool(BaseConnectionPool):
    """Pool for read only db users"""


parser = argparse.ArgumentParser()
parser.add_argument(
    "--ro",
    type=int,
    help='Number of read only connections',
    default=3
)

parser.add_argument(
    "--rw",
    type=int,
    help='Number of read and write connections',
    default=3
)

args = parser.parse_args()

ro_num = args.ro
rw_num = args.rw

read_only = ROPool(ro_num, **READ_ONLY_USER)
read_write = RWPool(rw_num, **READ_WRITE_USER)
