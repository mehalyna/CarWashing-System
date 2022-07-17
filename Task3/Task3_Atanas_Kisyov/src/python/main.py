import logging

import argparse
import psycopg2


AVAILABLE_TABLES = (
    'car_washes',
    'places',
    'car_wash_places',
    'services',
    'car_wash_services',
    'users',
    'accounts',
    'orders',
    'order_details',
)
INSTRUCTION_MESSAGE = 'This is a list of all available tables in the database. ' \
                      'Please make an input what you want to see.'


def add_arguments():
    """Initialize available arguments for user to pass to the program"""

    parser = argparse.ArgumentParser(prog='Database Connection')
    parser.add_argument('Mode', help='r=Read Mode, rw=Read/Write')
    args = vars(parser.parse_args())
    return args


class Singleton:
    """Base class to limit pools to one"""

    _instance = None

    def __new__(cls, *args: tuple, **kwargs: dict):
        """Create an instance only on first call"""

        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DatabaseConnection:
    """Database connection interface"""

    DATABASE = 'postgres'

    CONNECTION_SUCCESSFUL_LOGG_MESSAGE = 'Connection successful!'
    CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE = 'Connection failed! See exception message and try again!'

    def __init__(self):
        self.__connection = None

    def connect_to_database(self, username: str, password: str):
        """Establish connection using psycopg2"""

        try:
            self.__connection = psycopg2.connect(f"dbname={self.DATABASE} \
            user={username} password={password} host=localhost")
        except psycopg2.OperationalError as e:
            logging.critical(self.CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE)
            logging.critical(e)
            exit(1)

        logging.info(self.CONNECTION_SUCCESSFUL_LOGG_MESSAGE)
        return self.__connection


class ConnectionPool(Singleton):
    """Connection pool"""

    # Read-only username constants
    READ_ONLY_USERNAME = 'read_only_user'
    READ_ONLY_PASSWORD = 'unbreakable_password123'

    # Read/Write username constants
    READ_WRITE_USERNAM3 = 'read_write_user'
    READ_WRITE_PASSWORD = 'another_unbreakabale_password'

    def __init__(self) -> None:
        """Upon initialization, establish two connections (read-only and read/write) and add them to the pool"""

        super().__init__()

        connection = DatabaseConnection()
        self.read_only = connection.connect_to_database(self.READ_ONLY_USERNAME, self.READ_ONLY_PASSWORD)
        self.read_write = connection.connect_to_database(self.READ_WRITE_USERNAME, self.READ_WRITE_PASSWORD)

        # r -> read only, rw -> read/write
        self.pool = {
            'r': self.read_only,
            'rw': self.read_write
        }


if __name__ == '__main__':
    """Interact with user"""

    # Create pool
    pool = ConnectionPool()

    # Parse arguments
    parser = add_arguments()
    mode_type = parser['Mode']

    # Get connection
    try:
        connection = pool.pool[mode_type]
    except KeyError as e:
        logging.error(e.args)
        exit(1)
    
    # I tried to add some parameters to the queries, but it got really messy...
    # Thats why I left the hard-coded query
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts').fetchall()
