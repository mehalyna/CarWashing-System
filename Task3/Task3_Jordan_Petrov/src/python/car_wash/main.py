import logging
import sys

from src.python.car_wash.dbpool import ro_db_pool, rw_db_pool


def main():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)

    """Insert data into carwashes table"""
    with rw_db_pool.transaction() as cur:
        cur.execute('INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) '
                    'VALUES (%s, %s, %s)', ('testing', 'testing', 20))

    """Print all the rows from carwashes table"""
    with ro_db_pool.connection() as cur:
        cur.execute('SELECT * FROM carwashasdasdes;')
        for row in cur.fetchall():
            print(row)

if __name__ == '__main__':
    main()
