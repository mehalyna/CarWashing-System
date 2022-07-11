# Task2 - Jordan Petrov

The psql commands that I have uses are:
 - ```\c``` to connect to the database
 - ```\i``` to import the .sql files

And I am making sure that I start the terminal one directory before the db directory

## 1. Creating the db and it's tables

```psql -h localhost -U postgres < db/carwash/CREATE_DB.sql```

OUTPUT

```
CREATE DATABASE
You are now connected to database "carwashdb" as user "postgres".
CREATE TABLE
CREATE TABLE
CREATE TABLE
...
```

## 2. Inserting the data

```psql -h localhost -U postgres < db/carwash/INSERT_DATA.sql```

OUTPUT

```
You are now connected to database "carwashdb" as user "postgres".
INSERT 0 1
INSERT 0 1
INSERT 0 1
...
```
## 3. Check the database and it's data

```psql -h localhost -U postgres``` - Connecting to postgres

```\c carwashdb ``` - Connecting to carwashdb

```\dt``` - Display tables

OUTPUT

```
              List of relations
 Schema |       Name       | Type  |  Owner   
--------+------------------+-------+----------
 public | accounts         | table | postgres
 public | carwash_places   | table | postgres
 public | carwash_services | table | postgres
 public | carwashes        | table | postgres
 public | order_details    | table | postgres
 public | orders           | table | postgres
 public | places           | table | postgres
 public | services         | table | postgres
 public | users            | table | postgres
```

```SELECT * FROM users;```

OUTPUT

```
 user_id | phone_number |     full_name      |       user_location       
---------+--------------+--------------------+---------------------------
       1 | 473-491-4641 | Eada Elkins        | 996 Karstens Crossing
       2 | 268-223-4133 | Gennifer Alvarado  | 9693 Utah Circle
       3 | 697-104-1027 | Marian Grebert     | 195 Loomis Pass
       4 | 785-960-3220 | Valaria Eskriet    | 5 Bunker Hill Drive
       5 | 156-356-9947 | Wynn Faccini       | 2238 Charing Cross Circle
       6 | 374-662-3659 | Ellynn Dorrington  | 9 Crowley Junction
       7 | 827-220-2903 | Maridel Cottesford | 73 Coolidge Point
       8 | 293-356-0325 | Niles Kayser       | 447 Sheridan Crossing
       9 | 501-882-1380 | Travis Detheridge  | 54174 Union Junction
      10 | 112-408-3808 | Clarissa Sesons    | 2 Carberry Point
(10 rows)
```
