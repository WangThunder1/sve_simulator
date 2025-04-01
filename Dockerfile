FROM python:3.10-slim-buster

RUN apt-get update && \
  apt-get install -y \
    gcc \
    imagemagick \
    make \
    libpq-dev \
    wget

RUN mkdir -p /code /data
WORKDIR /code


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN wget -P . https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt && \
    rm -f /etc/ImageMagick-6/policy.xml && \
    apt-get purge -y gcc make && \
    apt-get autoremove -y 

COPY . /code/