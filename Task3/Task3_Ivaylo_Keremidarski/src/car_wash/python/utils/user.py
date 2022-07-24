import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--ro", type=int, action="store_true")
parser.add_argument("--rw", type=int, action="store_true")
args = parser.parse_args()

num_of_ro = args.ro
num_of_rw = args.rw

READ_ONLY_USER = {
    "hostname": "localhost",
    "username": "user",
    "password": "user",
    "_dbname": "car_wash_db",
    "pool_size": num_of_ro,
}

READ_WRITE_USER = {
    "hostname": "localhost",
    "username": "postgres",
    "password": "secret",
    "_dbname": "car_wash_db",
    "pool_size": num_of_rw,
}
