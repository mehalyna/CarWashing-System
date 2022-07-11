#Example of pool connections with psycopg2 


import psycopg2


connection_requirments = input()
query = input()

try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(
        **connection_requirments)
    if (postgreSQL_pool):
        print("Connection pool created successfully")

    conn = postgreSQL_pool.getconn()

    if (conn):
        with conn:
            with conn.cursor() as curs:
                curs.execute(query)
                data = curs.fetchall()


except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if postgreSQL_pool:
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")
