FROM python:3.10.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

COPY Carwash/ Carwash/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

