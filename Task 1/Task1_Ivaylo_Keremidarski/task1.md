# Task 1 - Ivaylo Keremidarski
## Run simple Python script in Docker

### 1. Build the Docker Image
```
docker build --tag test_app.py .
```

If you get a permission error:
```shell
sudo chmod 666 /var/run/docker.sock
```

Output
```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
test_app.py   latest    0cf7a4d758b4   46 hours ago   920MB
```

### 2. Create a Container
```shell
docker create --name simple_python_script test_app.py
```
Output
```
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                      PORTS     NAMES
ef11bd009eb3   test_app.py   "python3 ./test_app.…"   9 seconds ago   Created                               simple_python_script
```

### 3. Stop the container
```shell
ctrl + c
```