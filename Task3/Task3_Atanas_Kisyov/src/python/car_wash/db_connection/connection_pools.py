from collections import deque
import logging

import psycopg2

import PoolBaseClass

class ReadOnlyPool(PoolBaseClass):

    """Read-only connection pool"""

    CONNECTION_SUCCESSFUL_MESSAGE = 'Connection successful!'
    CONNECTION_UNSUCCESSFUL_MESSAGE = 'Connection failed! See exception message and try again!'
    SUCCESSFUL_CONNECTION_PULL_MESSAGE = 'A free connection is pulled from the pool!'
    CONNECTION_RETURNED_TO_POOL = 'Connection has been successfuly returned to the pool!'
    CONNECTION_ERROR_MESSAGE = 'There are no connections in the pool!'

    _pool = deque()

    def __init__(self, pool_size: int) -> None:
        self.pool_size = pool_size
        self._open_connection = None
    
    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""

        if self._pool:
            self._open_connection = self._pool.popleft()
            logging.info(self.SUCCESSFUL_CONNECTION_PULL_MESSAGE)
            return self._open_connection
        raise ConnectionError(self.VALIDATION_ERROR_MESSAGE)

    def __exit__(self) -> None:
        """Return database connection to the pool"""

        self._pool.append(self._current_connection)
        self._open_connection = None
        logging.info(self.CONNECTION_RETURNED_TO_POOL)
        return self._create_connection
    
    def _create_connection(self, hostname: str, username: str, password: str, database_name: str,) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        try:
            connection =  psycopg2.connect(dbname=database_name,
                                    user=username,
                                    password=password,
                                    host=hostname)
            logging.info(self.CONNECTION_SUCCESSFUL_MESSAGE)
            return connection
        except psycopg2.OperationalError as e:
            logging.critical(self.CONNECTION_UNSUCCESSFUL_MESSAGE)
            logging.critical(e.args)
            exit(1)
    
    def populate_pool(self, credentials: list) -> None:
        """Populate pool with read-only connections"""

        for user_credentials in credentials:
            connection = self._create_connection(*user_credentials)
            self._pool.append(connection)

        log_message = f'{self.pool_size} connections are added to the pool!'
        logging.info(log_message)


class ReadWritePool(ReadOnlyPool):

    """Read/Write connection pool"""

    _pool = []

    def __init__(self, pool_size: int) -> None:
        super().__init__(pool_size)
    
    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""

        return super().__enter__()
    
    def __exit__(self) -> None:
        """Return database connection to the pool"""

        return super().__exit__()
    
    def _create_connection(self, credentials: list) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        return super()._create_connection()
    
    def populate_pool(self, credentials: list) -> None:
        """Populate pool with read/write connections"""

        return super().populate_pool(credentials)
