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
## 3. Create an unstarted container
```
docker create --name my-python-script app.py
```
Check that the container is created
```
docker ps -a
```
OUTPUT
```
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                    PORTS     NAMES
1ee19dee3ca8   app.py               "python3 ./app.py"       3 minutes ago   Created                             my-python-script

```
## 4. Start the container
```
docker start my-python-script
```
## 5. Check the logs
```
docker logs -f my-python-script 
```
OUTPUT
```
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
INFO:my_first_docker_app:It works, go to the next iteration.
...
```
