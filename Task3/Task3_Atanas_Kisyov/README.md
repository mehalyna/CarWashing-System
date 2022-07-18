# Connect to PostgreSQL with Python

## 1. Clone the repository

```shell
git clone 'repository-link'
```

## 2. Create database

Enter psql console and input the following command and exit:

```shell
postgres=# CREATE DATABASE car_wash_db
```

## 3. Create tables

Execute the following command to create the tables from db/car_wash/schema

```shell
psql -h localhost -U postgres < CREATE_DB.sql
```

## 3. Insert data into tables

Execute the following command to insert data in the tables from db/car_wash/data

```shell
psql -h localhost -U postgres < INSERT_DATA.sql
```

## 4. View Table

Execute the following command to view the table contents of the database:

```shell
python3 src/python/main.py -ro 
```

## 5. Insert Data Into Table

Execute the following command to insert data into the tables:

```shell
python3 src/python/main.py -rw
```
