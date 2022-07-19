"""Main function for making queries to Car_Wash DB"""


import argparse

from libPyPool.utils import \
    Connection, Cursor, PoolReadConn, PoolWriteConn, create_pools


def main() -> None:
    """
    First: create pools
    Second: populate pools with connections
    Third: pull connection
    Fourth: give cursor and execute query in with statement
    Finally: push connection
    """

    # parameters for creating database connection
    params_dict = {
        'host': 'localhost',
        'port': 5432,
        'user': 'postgres',
        'password': 'pass',
        'dbname': 'postgres'
    }

    # create string of key word arguments from params_dict
    params = (" ").join(
        f"{key}={value}" for key, value in params_dict.items())

    # argument parser with argparse module
    parser = argparse.ArgumentParser()
    parser.add_argument("--ro", type=int,
                        help="Specify the size of pool with\
                             connections used for read only")
    parser.add_argument("--rw", type=int,
                        help="Specify the size of pool with\
                             connections used for read and write")
    args = parser.parse_args()
    if isinstance(args.ro, int):
        ro_num = args.ro
    else:
        ro_num = 3
    if isinstance(args.rw, int):
        rw_num = args.rw
    else:
        rw_num = 3

    pools = create_pools(ro_num, rw_num)    # create pools
    ro_pool = pools['ro']
    rw_pool = pools['rw']
    ro_name = PoolReadConn.__name__
    rw_name = PoolWriteConn.__name__

    for _ in range(ro_num):    # populate pools with connections
        with Connection(ro_name, params) as conn:
            ro_pool.push(conn)

    for _ in range(rw_num):    # populate pools with connections
        with Connection(rw_name, params) as conn:
            rw_pool.push(conn)

##############################################################################

    # with Cursor(rw_pool.pull()) as currs:
    #     currs.execute("Insert sql")

    # with Cursor(rw_pool.pull()) as currs:
    #     currs.execute("Select sql")
    #     data = currs.fetchall()
    #     print(data)


if __name__ == '__main__':
    main()
