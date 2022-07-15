import logging
import sys

import psycopg2
from psycopg2.extras import DictCursor


DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'carwashDB'
DB_USERNAME = 'bogdan'
DB_PASSWORD = '123456'

SQL_SELECT = 'SELECT * FROM "Users"'

CONNECTION_ERROR_MSG = 'Unsuccessful connection'


class CarWashConnection:
    def __init__(self, schema_name) -> None:
        self.schema_name = schema_name

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USERNAME,
                password=DB_PASSWORD,
                options=f"-c search_path={self.schema_name}",
                cursor_factory=DictCursor,
            )
            return self.conn
        except psycopg2.OperationalError as e:
            logging.info(CONNECTION_ERROR_MSG)
            logging.info(e)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.conn.close()


def main():
    def get_db(schema_name: str):
        return CarWashConnection(schema_name)

    with get_db("Users") as db:
        with db.cursor() as cursor:
            cursor.execute("some sql")


if __name__ == '__main__':
    sys.exit(main())
