"""Main file which executes the script"""
import sys
import logging

from config import USER_CREDENTIALS
from db_connection.connection_pools import ReadOnlyPool, ReadWritePool


def main():
    """Interact with user"""

    read_only_pool = ReadOnlyPool(**USER_CREDENTIALS)
    read_write_pool = ReadWritePool(**USER_CREDENTIALS)

    with read_write_pool.connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT...')

    with read_only_pool.connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        table = cursor.fetchall()
        for row in table:
            logging.info(row)


if __name__ == '__main__':
    sys.exit(main())
