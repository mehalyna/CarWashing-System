import logging

import psycopg2

class DatabaseConnection:

    """Database connection interface"""

    DATABASE = 'postgres'
    CONNECTION_SUCCESSFUL_LOGG_MESSAGE = 'Connection successful!'
    CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE = 'Connection failed! See exception message and try again!'
    CONNECTION_CLOSED_MESSAGE = 'Connection closed'

    def __init__(self, username, password):
        self.__connection = None
        self.username = username
        self.password = password

    def __enter__(self):
        """Establish connection using psycopg2"""

        try:
            self.__connection = psycopg2.connect(f"dbname={self.DATABASE} \
            user={self.username} password={self.password} host=localhost")
        except psycopg2.OperationalError as e:
            logging.critical(self.CONNECTION_UNSUCCESSFUL_LOGG_MESSAGE)
            logging.critical(e)
            exit(1)

        logging.info(self.CONNECTION_SUCCESSFUL_LOGG_MESSAGE)
        return self.__connection

    def __exit__(self):
        logging.info(self.CONNECTION_CLOSED_MESSAGE)
        return self.__connection.close()

