import psycopg2
from psycopg2 import pool


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DBConnectionPool:

    def __init__(self):
        self.pool = None

    def connect_to_db(self, host, port, dbname, user, password):
        try:
            self.pool = pool.SimpleConnectionPool(
                1, 10,
                user=user,
                password=password,
                host=host,
                port=port,
                database=dbname
            )
            return "Connected to DB"
        except (Exception, psycopg2.DatabaseError) as error:
            return error

    def get_connection(self):
        return self.pool.getconn()

    def return_connection(self, connection):
        return self.pool.putconn(connection)

    def execute_query(self, query):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.return_connection(connection)

        if type(result) is list:
            output = ""
            for row in result:
                output += str(row) + "\n"
            return output

        return result

if __name__ == '__main__':
    c1 = DBConnectionPool()
    print(c1.connect_to_db('localhost', 5432, 'carwashdb', 'postgres', 'admin'))
    print(c1.execute_query('SELECT * FROM carwashes'))
