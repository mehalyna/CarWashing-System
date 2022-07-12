##Run simple Python script in Docker

###Build a container
```shell
docker build --tag app.py . 
```
If you get an error "Got permission denied while trying to connect to the Docker daemon" run the following command and try again:
```shell
sudo chmod 666 /var/run/docker.sock
```

###Obtain IMAGE ID
```shell
docker images
```

###Output:

```
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
app.py       latest    bf70cf5ac987   5 days ago     920MB
```

###Create docker container with IMAGE ID

```shell
docker create bf70cf5ac987
```

###Obtain CONTAINER ID

```shell
docker ps -a
```

###Output:

```
CONTAINER ID   IMAGE          COMMAND              CREATED              STATUS    PORTS     NAMES
97a63cdb1a40   bf70cf5ac987   "python3 ./app.py"   About a minute ago   Created             priceless_poincare
```

###Start the container with CONTAINER ID

```shell
docker start 97a63cdb1a40
```

###Check what resources your container is using

```shell
docker stats
```

###Output:

```
CONTAINER ID   NAME                 CPU %     MEM USAGE / LIMIT     MEM %     NET I/O      BLOCK I/O    PIDS
97a63cdb1a40   priceless_poincare   0.00%     7.242MiB / 7.646GiB   0.09%     5.3kB / 0B   0B / 639kB   1
```

###See logs

```shell
docker logs -f 97a63cdb1a40
```

###Output:

```
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
```
