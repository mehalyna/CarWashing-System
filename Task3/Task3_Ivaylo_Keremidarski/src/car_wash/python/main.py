import sys
import logging
from connection.pool import ro_pool, rw_pool


def main():
    """Configure log"""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)

    """Insert data into carwashes table"""
    with rw_pool as cur:
        cur.execute(
            "INSERT INTO carwashes (carwash_name, carwash_address, quantity_of_places) "
            "VALUES (%s, %s, %s)",
            ("carwash1", "address1", 1),
        )

    """Print all the rows from carwashes table"""
    with ro_pool as cur:
        cur.execute("SELECT * FROM carwashes;")
        for row in cur.fetchall():
            print(row)


if __name__ == "__main__":
    sys.exit(main)
