import logging

from db_connection import ConnectionPool
from utils.parse_arguments import add_arguments


def main():
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


if __name__ == '__main__':
    main()