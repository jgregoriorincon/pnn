FROM python:3.9.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql-client \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal

RUN apt-get install -y libgdal-dev g++ --no-install-recommends \
    && apt-get clean -y

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static

WORKDIR /app
USER app_user:app_user
COPY --chown=app_user:app_user . .
RUN chmod +x docker/*.sh

ENTRYPOINT [ "docker/entrypoint.sh" ]
CMD [ "docker/start.sh", "server" ]
