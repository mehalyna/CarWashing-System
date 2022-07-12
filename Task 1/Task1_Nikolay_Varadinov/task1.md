#### Build image from dockerfile:
- first: takes python:3.10.5-slim-buster image.
- second: from the first image and with app.py creates py-app-docker image:

`docker image build --tag py-app-docker .`

#### With --rm for removing the container after run it:

`docker run --rm py-app-docker` 

#### To create container without run it:

`docker container create py-app-docker`

#### Take container id:

`docker container ls -a`

#### To run it with -a for attaching STDOUT/STDERR:

`docker container start -a CONTAINER_ID`

#### or run and follow logs with:

`docker logs -f CONTAINER_ID`
