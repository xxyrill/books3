# pull base image
FROM python:3.12.2

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# install psycopg2
RUN pip install psycopg2-binary

# copy project
COPY . /code/