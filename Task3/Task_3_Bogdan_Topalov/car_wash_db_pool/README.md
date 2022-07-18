## Steps to execute 
...

## Pull Postgres image
```docker pull postgres```

## Run the Docker container
```
docker run 
    --name PostgresContainer 
    -p 5455:5432 
    -e POSTGRES_USER=bogdan 
    -e POSTGRES_PASSWORD=123456 
    -e POSTGRES_DB=carwashDB 
    -d 
    postgres
```

**The environment variables above can be checked with:**
```docker exec PostgresContainer env```

