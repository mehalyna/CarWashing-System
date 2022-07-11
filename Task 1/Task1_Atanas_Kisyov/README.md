### Run simple Python script in Docker

1. Build an image
```shell
docker build --tag app.py . 
```
If you get an error "Got permission denied while trying to connect to the Docker daemon" run the following command and try again:
```shell
sudo chmod 666 /var/run/docker.sock
```

2. Run
```shell
docker run app.py
```
