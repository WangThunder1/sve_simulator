FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye

RUN apt-get update && \
  apt-get install -y \
    gcc \
    imagemagick \
    make \
    libpq-dev \
    wget

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN wget -P ./code https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem

