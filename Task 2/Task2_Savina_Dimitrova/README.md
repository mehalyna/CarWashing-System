# Task 2



## First Steps

Make sure postgresql is pulled.

```bash
docker pull postgres:latest
```
Then create docker-compose.yml file
```bash
version: '3.8'
services:
  db:
    container_name: pg_container
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: test_db
    ports:
      - "5432:5432"
  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - "5050:80"
```
Then, connect to that file using docker-compose up.
```bash
docker compose up
```
After that, pgadmin4 opens on http://localhost:5050/, in which enter details from docker-compose.yml.
