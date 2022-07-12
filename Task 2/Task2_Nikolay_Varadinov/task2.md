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
