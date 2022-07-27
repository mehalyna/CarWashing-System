"""User file"""

from cw_main import cw_pools

pools = cw_pools()
rw_pool = pools['rw_pool']
ro_pool = pools['ro_pool']

with rw_pool.transaction() as curs:
    curs.execute("DELETE FROM table_name")

with rw_pool.transaction() as curs:
    curs.execute("INSERT INTO table_name (content) VALUES ('New')")
    curs.execute("INSERT INTO table_name (content) VALUES ('one')")
    curs.execute("INSERT INTO table_name (content) VALUES ('here')")

with ro_pool.transaction() as curs:
    curs.execute("SELECT * FROM table_name")
    data = curs.fetchall()
    for line in data:
        print(line, '\n')

with rw_pool.transaction() as curs:
    curs.execute("INSERT INTO table_name (content) VALUES ('New')")
    curs.execute("INSERT INTO table_name (content) VALUES ('one')")
    curs.execute("INSERT INTO table_name (content) VALUES ('here')")

with ro_pool.transaction() as curs:
    curs.execute("SELECT * FROM table_name")
    data = curs.fetchall()
    for line in data:
        print(line, '\n')
