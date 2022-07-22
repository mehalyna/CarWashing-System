from src.python.car_wash.pool import read_only, read_write


def main():
    """Insert data into carwashes table"""
    with read_write as cur:
        cur.execute('INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) '
                    'VALUES (%s, %s, %s)', ('testing', 'testing', 20))

    """Print all the rows from carwashes table"""
    with read_only as cur:
        cur.execute('SELECT * FROM carwashes;')
        for row in cur.fetchall():
            print(row)


if __name__ == '__main__':
    main()
