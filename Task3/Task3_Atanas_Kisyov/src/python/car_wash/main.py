from python.car_wash.db_connection.connection_pools import ReadOnlyPool, ReadWritePool
from utils.parse_arguments import add_arguments
from utils.credentials import read_user_credentials


def main():
    """Interact with user"""

    #  Get arguments from user command
    connection_options = add_arguments()

    # User credentials for database connections
    read_only_users = read_user_credentials('read_only_users.csv')
    read_write_users = read_user_credentials('read_write_users.csv')

    # Create connection pools
    read_only_pool = ReadOnlyPool(5)
    read_write_pool = ReadWritePool(5)

    # Populate the connection pools
    read_only_pool.populate_pool(read_only_users)
    read_write_pool.populate_pool(read_write_users)

    pools = {
        '-ro': read_only_pool,
        '-rw': read_write_pool,
    }

    choosen_connection_type = connection_options.get('-ro, -rw', '-ro')
    choosen_connection = pools.get(choosen_connection_type)

    with choosen_connection as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM accounts').fetchall()


if __name__ == '__main__':
    main()