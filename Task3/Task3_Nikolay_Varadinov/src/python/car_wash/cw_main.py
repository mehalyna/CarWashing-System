"""Main function for making queries to Car_Wash DB"""


import argparse
import logging

from py_pool_lib.py_pool import PoolReadConn, PoolWriteConn
from db_config.car_wash_db_config import CAR_WASH_DB_CONFIG as CW_DB


print("Use CW_DB as Car_Wash database configuration.")
print("Pool sizes given as rw_pool: int and ro_pool: int")

def cw_pools():
    """Returns dictionary with pools for CAR_WASH DB."""

    return {'ro_pool': PoolReadConn(3, CW_DB),
            'rw_pool': PoolWriteConn(3, CW_DB)}

def basic_ro_pool_manager(queiry: str, pool: PoolReadConn):
    """Executes some read-only queiries."""

    with pool.transaction() as curs:
        curs.execute(queiry)
        data = curs.fetchall()
        logging.info("READ")
        for line in data:
            print(line, "\n")


def basic_rw_pool_manager(quiery: str, pool: PoolWriteConn):
    """Executes some write queiris."""

    with pool.transaction() as curs:
        curs.execute(quiery)

def main1(ro_num=3, rw_num=3) -> None:
    """
    Can take some sql queiries from terminal.
    Create two pools:
        ro_pool - read-only and,
        rw_pool - write and read
    """

    flag = False

    # Primitive control loop
    while not flag:
        which_db = input("Use CarWash DB: Y/N?  ")
        if which_db == "Y":
            db_config = CW_DB
        else:
            db_config = input("Enter parameters without comma.")
            db_config = {k: v.replace("'", "") for [k, v] in
                         [kw.split('=') for kw in db_config.split(' ')]}

        ro_pool_in = PoolReadConn(ro_num, db_config)
        rw_pool_in = PoolWriteConn(rw_num, db_config)

        stop_command = input("Press q to exit or continue with enter.   ")
        if stop_command == 'q':
            break

        change_db = input("Ask me about DB again: Y?   ")
        working = True
        while working:
            if change_db == "Y":
                working = False
            pool_type = input("Read or write: R/W?  ")
            queiry = input("Enter your queiry:   ")
            execute = input("Execute: Y/N?   ")

            if execute == 'Y':
                if pool_type == 'R':
                    if queiry:
                        basic_ro_pool_manager(queiry, ro_pool_in)

            if execute == 'Y':
                if pool_type == 'W':
                    if queiry:
                        basic_rw_pool_manager(queiry, rw_pool_in)

            stop_command = input("Press q to exit or continue with enter.   ")
            if stop_command == 'q':
                flag = True
                break

if __name__ == '__main__':

    # Primitive argument parser with argparse module
    parser = argparse.ArgumentParser()
    parser.add_argument("--ro", type=int,
                        help="Specify the size of pool with\
                             connections used for read only")
    parser.add_argument("--rw", type=int,
                        help="Specify the size of pool with\
                             connections used for read and write")
    args = parser.parse_args()
    if isinstance(args.ro, int):
        RO_NUM = args.ro
    else:
        RO_NUM = 3
    if isinstance(args.rw, int):
        RW_NUM = args.rw
    else:
        RW_NUM = 3

    main1(RO_NUM, RW_NUM)
