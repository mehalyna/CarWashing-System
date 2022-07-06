
 #Accesing Postgres
 
 svetoslav@svet:~/Desktop$ psql -U postgres

postgres=#

# All the databases
postgres=# \l
 
                                   List of databases
 
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 Carwash   | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
 postgres  | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
 template0 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
(5 rows)


#Accessing Carwash
postgres=# \c Carwash
Carwash=#

#All tables in Carwash
Carwash=# \dt

              List of relations
 Schema |       Name       | Type  |  Owner   
--------+------------------+-------+----------
 public | accounts         | table | postgres
 public | carwash_places   | table | postgres
 public | carwash_services | table | postgres
 public | carwhashes       | table | postgres
 public | order_details    | table | postgres
 public | orders           | table | postgres
 public | places           | table | postgres
 public | services         | table | postgres
 public | users            | table | postgres
(9 rows)

Carwash=# 

