Ivaylo Keremidarski
# Task 2 - Run Postgres Docker Container. Play with Data

### 1. Run Postgres in a Docker Container
```
$ docker container run -d --name=pg -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata -v /pgdata:/pgdata postgres:14.4
```

Check the Container:
```
docker container ls
```
Output:
```
output
```

If you don't have `psql`:
```
$ sudo apt-get update
$ sudo apt install postgresql postgresql-contrib 
```

### 2. Connect to PostgresSQL
```
$ psql -h localhost -p 5432 -U postgres
```
Output
```
postgres=#
```

### 3. Create a database
```
$ 
```

