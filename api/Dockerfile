FROM python:3.9-slim-buster

RUN apt-get update

RUN mkdir -p /api
WORKDIR /api
ADD requirements.txt ./requirements.txt
RUN  python -m pip install -U pip && pip install -r requirements.txt
COPY . /api

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
