# Task1 - Jordan Petrov

First think is to pull the postgres image from the docker hub.
```
docker pull postgres:alpine
```
Than I check my images.
```
docker images
```
OUPUT:
```
REPOSITORY      TAG         IMAGE ID       CREATED        SIZE
postgres        alpine      07c710d28b91   13 days ago    216MB
```
To start that instance.
```
docker run --name softserve-academy-db -e POSTGRES_PASSWORD=admin -d -p 5432:5432 postgres:alpine
```
Check if the container is running.
```
docker ps
```
OUTPUT
```
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                       NAMES
6a3e0bb970d0   postgres:alpine   "docker-entrypoint.s…"   9 seconds ago   Up 6 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   softserve-academy-db
```
Bashing into the container.
```
docker exec -it softserve-academy-db bash
```
Getting the Postgres user.
```
\du
```
OUTPUT
```
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

```
Getting the root access of psql.
```
psql -U postgres
```
So now I have access to all psql commands and I can create db.
Creating a db.
```
create database carwashdb;
```
See all the databases.
```
\l
```
OUTPUT
```
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 carwashdb | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

```
