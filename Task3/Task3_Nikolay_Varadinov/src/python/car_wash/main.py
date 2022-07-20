"""Main function for making queries to Car_Wash DB"""


import argparse

from libPyPool.utils import Cursor, PoolReadConn, PoolWriteConn
from dbpool import CAR_WASH_DB_CONFIG as db_config


def main() -> None:
    """
    First: create pools
    Second: populate pools with connections
    Third: pull connection from pool
    Fourth: set cursor and execute query in with statement
    Finally: push connection
    """

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


    ro_pool = PoolReadConn(ro_num, db_config)  # Could be called with key word args
    rw_pool = PoolWriteConn(rw_num, db_config) # Could be called with key word args
    ro_pool.populate_pool()
    rw_pool.populate_pool()


##############################################################################

#     conn1 = ro_pool.pull()
#     conn2 = ro_pool.pull()
#     conn3 = ro_pool.pull()

#     with Cursor(conn1) as currs:
#         currs.execute("INSERT INTO table_name (content) VALUES ('LET')")

#     with Cursor(conn2) as currs:
#         currs.execute("INSERT INTO table_name (content) VALUES ('SEE')")

#     with Cursor(conn3) as currs:
#         currs.execute("INSERT INTO table_name (content) VALUES ('THIS')")

#     with Cursor(ro_pool.pull()) as currs:
#         currs.execute("SELECT * FROM table_name")
#         data = currs.fetchall()
#         print(data)


if __name__ == '__main__':
    main()
