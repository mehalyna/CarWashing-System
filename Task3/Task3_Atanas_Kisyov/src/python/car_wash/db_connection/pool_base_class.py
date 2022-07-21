"""Abstract base class to ensure that database pools implement the correct methods"""
import psycopg2

from python.car_wash.utils.singleton import Singleton


class PoolBaseClass(metaclass=Singleton):

    """Abstract base class for creating connection pools"""

    def __enter__(self) -> psycopg2.connect:
        """Get database connection from pool"""
        raise NotImplementedError('Method is not implemented in child class!')
    
    def __exit__(self) -> None:
        """Return database connection to the pool"""
        raise NotImplementedError('Method is not implemented in child class!')

    def _create_connection(self) -> psycopg2.connect:
        """Create connection and add it to the pool"""
        raise NotImplementedError('Method is not implemented in child class!')
    
    def _populate_pool(self) -> None:
        """Populate pool with connections"""
        raise NotImplementedError('Method is not implemented in child class!')
