"""Fill this in constants with your db connection parameters."""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--ro",
    type=int,
    help='Number of read only connections',
    default=3
)

parser.add_argument(
    "--rw",
    type=int,
    help='Number of read and write connections',
    default=3
)

args = parser.parse_args()

ro_num = args.ro
rw_num = args.rw

READ_ONLY_USER = {
    'hostname': 'localhost',
    'username': 'car_wash_user',
    'password': 'user',
    '_dbname': 'carwashdb',
    'pool_size': ro_num,
}

READ_WRITE_USER = {
    'hostname': 'localhost',
    'username': 'postgres',
    'password': 'admin',
    '_dbname': 'carwashdb',
    'pool_size': rw_num,
}
