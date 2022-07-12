#Execute SQL using psql

##1. Create database
```shell
postgres=# CREATE DATABASE car_wash_db
```
##2. Create tables
```shell
psql -h localhost -U postgres < CREATE_DB.sql
```
##3. Insert data into tables
```shell
psql -h localhost -U postgres < INSERT_DATA.sql
```
