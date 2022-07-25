import argparse
import logging
import sys

from src.python.car_wash.config import RO_USER, RW_USER
from src.python.car_wash.pool import rw_pool_helper, ro_pool_helper, RODBPool, RWDBPool

"""Test query"""

QUERY = "SELECT * FROM users"
INSERT = "INSERT INTO users (user_id, phone_number, full_name, user_location) " \
         "VALUES (123, 32334442039, 'Pesho Ivanov', 'Sofia')"


def main():
    
    logger = logging.getLogger()
    fhandler = logging.FileHandler(filename='mylog.log', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    logger.setLevel(logging.DEBUG)

    """Print all the rows from users table"""
    with rw_pool_helper.rw_pool() as (cursor, _):
        cursor.execute(QUERY)
        for record in cursor.fetchall():
            print(record)

    """Insert data into carwashes table"""
    with ro_pool_helper.ro_pool() as (cursor, _):
        cursor.execute(INSERT)
        logging.info('Data inserted.')


parser = argparse.ArgumentParser()
parser.add_argument(
    "--ro",
    type=int,
    default=3
)

parser.add_argument(
    "--rw",
    type=int,
    default=3
)

args = parser.parse_args()

ro_conns = args.ro
rw_conns = args.rw

read_only = RODBPool(ro_conns, **RO_USER)
read_write = RWDBPool(rw_conns, **RW_USER)

if __name__ == '__main__':
    sys.exit(main())
