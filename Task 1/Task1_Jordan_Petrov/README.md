# Task1 - Jordan Petrov

## 1. Build an image
```
docker build --tag app.py .
```
## 2. Check the images
```
docker images
```
OUTPUT
```
REPOSITORY      TAG              IMAGE ID       CREATED         SIZE
app.py          latest           577aea6d18c4   2 minutes ago   45.2MB
```
## 3. Run the container
```
docker run --publish 800:800 app.py
```

If I open another terminal and check the list of running containers
```
docker ps
```
OUTPUT
```
CONTAINER ID   IMAGE     COMMAND              CREATED              STATUS              PORTS                                       NAMES
d8eecdb7d235   app.py    "python3 ./app.py"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   charming_wu
```
