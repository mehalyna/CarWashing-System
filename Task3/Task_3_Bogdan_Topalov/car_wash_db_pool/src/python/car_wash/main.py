import logging

from car_wash_db_pool.src.python.car_wash.db.db_pool import ro_db_pool, rw_db_pool


SQL_SELECT = 'SELECT * FROM "Users"'
SQL_INSERT = 'INSERT INTO "Users"' \
             '(user_id, phone_number, full_name, user_location)' \
             'VALUES ' \
             '(1, "0888888888", "Bogdan Topalov", "Somewhere"),'


def main():

    """Select all rows from "Users" and log it"""
    with ro_db_pool.connection() as cursor:
        cursor.execute(SQL_SELECT)
        for r in cursor.fetchall():
            logging.info(r)

    """Insert data into "Users" table"""
    with rw_db_pool.connection() as cursor:
        cursor.execute(SQL_INSERT)
        logging.info('Inserted data into "Users" table.')


if __name__ == '__main__':
    main()
