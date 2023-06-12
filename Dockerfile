FROM python:3.10-slim

RUN mkdir /app

COPY requirements.txt /app

COPY ./ /app

WORKDIR /app

EXPOSE 8000

RUN pip install -r /app/requirements.txt --no-cache-dir

RUN adduser --disabled-password app-user

USER app-user

