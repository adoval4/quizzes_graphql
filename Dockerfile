FROM python:3

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE=src.settings
ENV COMPOSE_HTTP_TIMEOUT=20000

RUN apt-get update

EXPOSE 8000

RUN mkdir /code
COPY django/project /code

WORKDIR /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
