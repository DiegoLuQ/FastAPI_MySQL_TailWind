FROM python:3.9-slim-buster

WORKDIR /app_d

COPY ./app/requirements.txt /app_d/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app_d/requirements.txt

COPY ./app /app_d/