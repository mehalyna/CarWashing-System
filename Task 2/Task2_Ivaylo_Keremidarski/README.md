Ivaylo Keremidarski
# Task 2 - Run Postgres Docker Container. Play with Data

### 1. Run Postgres in a Docker Container
```
$ docker container run -d --name=pg -p 5432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata -v /pgdata:/pgdata postgres:14.4
```

Output
```
output
```

