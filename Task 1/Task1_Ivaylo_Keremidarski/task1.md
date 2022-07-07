# Task 1
## Run simple Python script in Docker

### 1. Build the container:
```shell
docker build --tag test_app.py . 
```

If you get a permission error:
```shell
sudo chmod 666 /var/run/docker.sock
```

### 2. Run the container
```shell
docker run --publish 5001:5001 test_app.py
```

### 3. Stop the container
```shell
ctrl + c
```
