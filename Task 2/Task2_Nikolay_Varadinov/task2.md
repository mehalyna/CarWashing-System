#### Run PostgreSQL in docker with:

`docker run --name 'container name' -p 'some port':5432 -e POSTGRES_USER='user name' -e POSTGRES_PASSWORD='pswd' -e POSTGRES_DB='db name' -d postgres`  
> May use yml file insted of configurating in docker command.
 
 #### Connect with:
 
`psql -h localhost -p 'port' -U 'user name' -d postgres`
  
#### Create DB with:

`psql> create database 'db name'`  
> `psql> \c 'db name'`  - connect to database  
> `psql> \l` - list databases

#### Create tables and insert data from sql file with:

`psql -h 'localhost' -p 'port' -d 'db name' -U 'user name' < 'file.sql'`  

#### Show TABLES:

```
db=# \dt
                List of relations
 Schema |       Name       | Type  |    Owner     
--------+------------------+-------+--------------
 public | accounts         | table | postgresUser
 public | carwash_places   | table | postgresUser
 public | carwash_services | table | postgresUser
 public | carwashes        | table | postgresUser
 public | order_details    | table | postgresUser
 public | orders           | table | postgresUser
 public | places           | table | postgresUser
 public | services         | table | postgresUser
 public | users            | table | postgresUser
```
#### Join TABLES:

```
db=# SELECT full_name, email FROM accounts JOIN users ON accounts.user_id=users.user_id;
    full_name    |       email       
-----------------+-------------------
 Ivan Petrov     | ivan@ivan.com
 Georgi Stoyanov | georgi@georgi.com
 Maria Vlahova   | maria@maria.com
```
