import logging
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


class Singleton:
    """Base class to limit open connections to one"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create an instance only on first call"""

        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DatabaseConnection(Singleton):
    """Database connection interface"""

    DATABASE = 'postgres'
    USER = 'postgres'
    PASSWORD = '1123QwER'

    CONNECTION_SUCCESSFUL_LOGG_MESSAGE = 'Connection successful!'
    CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE = 'Connection failed! See exception message and try again!'

    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect_to_database(self):
        """Establish connection using psycopg2"""

        try:
            self.__connection = psycopg2.connect(
                database=self.DATABASE,
                user=self.USER,
                password=self.PASSWORD,
            )
        except psycopg2.OperationalError as e:
            logging.critical(self.CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE)
            logging.critical(e)
            exit(1)

        logging.info(self.CONNECTION_SUCCESSFUL_LOGG_MESSAGE)
        return self.__connection

    def create_cursor(self):
        """Create connection cursor"""
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def close_connection(self):
        """Close connection"""
        return self.__connection.close


class ViewTable(DatabaseConnection):
    """User interface"""

    def view_table(self, table):
        """Method takes table name(string) and column names (list)"""
        
        # Error handling for wrong input
        if table not in AVAILABLE_TABLES:
            raise ValueError('Table does not exist!')

        select_sql_statement = f'SELECT * FROM {table}'
        return self.__cursor.execute(select_sql_statement)


if __name__ == '__main__':

    # Establish connection
    connection = ViewTable()
    connection.connect_to_database()
    connection.create_cursor()

    # Log the available tables
    logging.info(INSTRUCTION_MESSAGE)
    logging.info(', '.join(AVAILABLE_TABLES))

    # User input
    command = input()

    # Print table contents
    table_contents = connection.view_table(command)
    logging.info(table_contents)
