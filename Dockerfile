FROM python:slim

LABEL maintainer="smaeil0018@gmail.com"
LABEL version="1.0"
LABEL description="Cinema eng"

ENV PYTHONPATH=. TZ="Asia/Tehran" 

WORKDIR /usr/src/app

COPY pyproject.toml ./

RUN pip install --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . .