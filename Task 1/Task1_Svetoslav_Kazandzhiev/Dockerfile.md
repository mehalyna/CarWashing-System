FROM ubuntu:latest

WORKDIR /usr/app/src

COPY app.py ./

CMD [ "python3", "./app.py"]
