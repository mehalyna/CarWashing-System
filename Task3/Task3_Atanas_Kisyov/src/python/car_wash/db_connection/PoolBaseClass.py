import logging

import psycopg2

import Singleton

class PoolBaseClass(metaclass=Singleton):

    """Abstract base class for creating connection pools"""
    
    NOT_IMPLEMENTED_ERROR = 'Method is not implemented in child class!'

    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""

        raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)
    
    def __exit__(self) -> None:
        """Return database connection to the pool"""

        raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)

    def _create_connection(self) -> psycopg2.connect:
        """Create connection and add it to the pool"""

        raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)
    
    def _populate_pool(self) -> None:
        """Populate pool with connections"""

        raise NotImplementedError(self.NOT_IMPLEMENTED_ERROR)