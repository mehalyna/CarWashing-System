### Run simple Python script in Docker

1. Build a container
```shell
docker build --tag app.py . 
```
If you get an error "Got permission denied while trying to connect to the Docker daemon" run the following command and try again:
```shell
sudo chmod 666 /var/run/docker.sock
```

2. Run the container
```shell
docker run --publish 5001:5001 app.py
```