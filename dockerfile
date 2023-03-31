FROM python:3.9-slim-buster

RUN apt-get update &&  apt-get install -y cmake build-essential &&  apt-get install -y default-libmysqlclient-dev  && apt-get install -y libgl1-mesa-glx


RUN mkdir /app
WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt



COPY . /app

ENV PYTHONUNBUFFERED 1
#ENV DATABASE_URL=mysql://mysql:mysql@localhost:3306/mysql

