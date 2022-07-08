# Task 1: 

Run simple Python script in Docker

## Commands

Use docker build to create the image from the app.py file and Dockerfile

```bash
$ docker build -t pytask1 .
```
Then use docker create to create the container from the image and name it.
```bash
$ docker create --name task1container pytask1
```
Use docker start to start the container created earlier
```bash
$ docker start task1container
```
To check the logs of the container:
```bash
$ docker logs -f task1container
```
