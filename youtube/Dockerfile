FROM python:3.11.2-slim-buster

ENV WORKDIR=youtube
WORKDIR "/$WORKDIR"

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/${WORKDIR}/app/"