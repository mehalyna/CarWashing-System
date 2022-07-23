import logging

from db_connection.config import USER_CREDENTIALS
from db_connection.connection_pools import ReadOnlyPool, ReadWritePool
from utils.parse_arguments import add_arguments


def main():
    """Interact with user"""

    #  Get arguments from user command
    connection_options = add_arguments()
    arg = {'arg': key for key, value in connection_options.items() if value}
    arg = arg.get('arg', 'ro')

    # Create connection pools
    read_only_pool = ReadOnlyPool(**USER_CREDENTIALS, pool_size=5)
    read_write_pool = ReadWritePool(**USER_CREDENTIALS, pool_size=2)

    # Populate the connection pools
    read_only_pool.populate_pool()
    read_write_pool.populate_pool()

    pools = {
        'ro': read_only_pool,
        'rw': read_write_pool,
    }

    choosen_connection = pools.get(arg)

    with choosen_connection.connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        table = cursor.fetchall()
        for row in table:
            print(row)


if __name__ == '__main__':
    main()
