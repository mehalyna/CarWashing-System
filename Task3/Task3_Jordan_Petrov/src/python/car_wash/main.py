import logging
import sys

from car_wash.dbpool import ro_db_pool, rw_db_pool


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(message)s')
    log = logging.getLogger('db_pool')

    """Insert data into carwashes table"""
    with rw_db_pool.transaction() as cur:
        cur.execute('INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) '
                    'VALUES (%s, %s, %s)', ('testing', 'testing', 20))

    """Print all the rows from carwashes table"""
    with ro_db_pool.connection() as cur:
        cur.execute('SELECT * FROM carwashes;')
        for row in cur.fetchall():
            log.info(row)


if __name__ == '__main__':
    sys.exit(main())
