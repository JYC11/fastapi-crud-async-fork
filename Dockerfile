# pull official base image
FROM python:3.11.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/

RUN pip install pipenv

RUN pipenv sync

