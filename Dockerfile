FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /periodicTable

ADD ./periodicTable

COPY ./periodicTable

CDM ["python", "periodicTable/manage.py"]


