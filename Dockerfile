FROM python:3.12

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir Flask 

WORKDIR /app/remonitor

COPY ./app /app/remonitor

WORKDIR /app