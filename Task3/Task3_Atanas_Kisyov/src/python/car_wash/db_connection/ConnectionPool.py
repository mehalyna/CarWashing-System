import logging

import DatabaseConnection
import Singleton

class ConnectionPool(metaclass=Singleton):

    """Connection pool"""

    # Read-only username constants
    READ_ONLY_USERNAME = 'read_only_user'
    READ_ONLY_PASSWORD = 'unbreakable_password123'

    # Read/Write username constants
    READ_WRITE_USERNAME = 'read_write_user'
    READ_WRITE_PASSWORD = 'another_unbreakabale_password'

    def __init__(self, connection_count=3) -> None:
        """Upon initialization, establish two connections (read-only and read/write) and add them to the pool"""

        self.connection_count = connection_count

        # Postgres users and passwords should be stored in a file and taken from there
        # Also both instance variables should be a list of DatabaseConnection instances

        self.read_only_connections = DatabaseConnection(self.READ_ONLY_USERNAME, self.READ_ONLY_PASSWORD)
        self.read_write_connections = DatabaseConnection(self.READ_WRITE_USERNAME, self.READ_WRITE_PASSWORD)

        # r -> read only, rw -> read/write
        self.pool = {
            'r': self.read_only,
            'rw': self.read_write
        }
