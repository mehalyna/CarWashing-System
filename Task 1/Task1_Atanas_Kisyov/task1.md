docker-compose.yml
```dockerfile
version: '3.4'

services:
  postgres:    
    image: postgres
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: 1123QwER
      POSTGRES_USER: postgres
      POSTGRES_DB: postgres
      PGDATA: /var/lib/postgresql/data/pgdata
    volumes:
      - ./postgresql:/var/lib/postgresql/data
```

Log in as root:

```shell
atanaskisyov@pop-os:~/coding$ sudo su root
root@pop-os:/home/atanaskisyov/coding# 
```

Start docker container:
```shell
atanaskisyov@pop-os:~/coding$ sudo su root
root@pop-os:/home/atanaskisyov/coding# docker-compose up -d
coding_postgres_1 is up-to-date
root@pop-os:/home/atanaskisyov/coding# 
```
Enter postgres console:
```shell
root@pop-os:/home/atanaskisyov/coding# docker exec -ti "coding_postgres_1" psql -U "postgres"
psql (14.1 (Debian 14.1-1.pgdg110+1))
Type "help" for help.

postgres=# 
```


```shell
atanaskisyov@pop-os:~/coding$ sudo su root
root@pop-os:/home/atanaskisyov/coding# docker-compose up -d
coding_postgres_1 is up-to-date
root@pop-os:/home/atanaskisyov/coding# docker exec -ti "coding_postgres_1" psql -U "postgres"
psql (14.1 (Debian 14.1-1.pgdg110+1))
Type "help" for help.
postgres=# \d
               List of relations
 Schema |       Name        | Type  |  Owner   
--------+-------------------+-------+----------
 public | accounts          | table | postgres
 public | car_wash          | table | postgres
 public | car_wash_places   | table | postgres
 public | car_wash_services | table | postgres
 public | order_details     | table | postgres
 public | orders            | table | postgres
 public | places            | table | postgres
 public | services          | table | postgres
 public | users             | table | postgres
(9 rows)

postgres=# 
```

Table details:

```shell
postgres=#  \d accounts
                       Table "public.accounts"
   Column   |          Type          | Collation | Nullable | Default 
------------+------------------------+-----------+----------+---------
 account_id | integer                |           | not null | 
 user_id    | integer                |           |          | 
 email      | character varying(50)  |           |          | 
 password   | character varying(100) |           |          | 
Indexes:
    "accounts_pkey" PRIMARY KEY, btree (account_id)
Foreign-key constraints:
    "fk_user_id" FOREIGN KEY (user_id) REFERENCES users(user_id)

postgres=#
```

