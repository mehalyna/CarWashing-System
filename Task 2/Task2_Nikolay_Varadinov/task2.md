Run PostgreSQL in docker with:

  docker run --name 'container name' -p 'some port':5432 -e POSTGRES_USER='user name' -e POSTGRES_PASSWORD='pswd' -e POSTGRES_DB='db name' -d postgres
  # May use yml file insted of configurating in docker command.
 
 Connect with:
 
  psql -h localhost -p 'port' -U 'user name' -d postgres
  
Create DB with:

  psql> create database 'db name'

Create tables and insert data with:

  psql -h 'localhost' -p 'port' -d 'db name' -U 'user name' < 'path/sql file'
