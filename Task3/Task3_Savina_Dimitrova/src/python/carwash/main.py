"""Main user interface for executing queries or accessing the database connection pool"""
import logging
import sys

from psycopg2 import cursor
from src.python.carwash.DB_connections.dbpoolmanager import ro_db_pool, rw_db_pool


logging.basicConfig(format = '%(process)d-%(levelname)s-%(message)s')


"""Two exmaple queries for testing and demonstration purposes"""
SELECT_QUERY = 'SELECT * FROM users'
INSERT_QUERY = 'INSERT INTO users (user_id, phone_number, full_name, user_location' \
                'VALUES (2, 359123456789, "Ivan Ivanov", "Plovdiv")'

def main():
    """Using the ReadWrite pool, insert data into Users table"""
    conRW = rw_db_pool.connection() 
    with conRW as cursor:
        cursor.execute(INSERT_QUERY)

        logging.info("Query inserted.")

    """Using the ReadOnly pool, view the table data from users table"""
    conRO = ro_db_pool.connection()
    with conRO as cursor:
        cursor.execute(SELECT_QUERY)

        for r in cursor.fetchall():
            logging.info(r)


if __name__ == '__main__':
    sys.exit(main)