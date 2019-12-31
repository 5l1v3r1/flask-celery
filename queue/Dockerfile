FROM python:3.8.1-alpine3.11

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir  -r requirements.txt

ENTRYPOINT celery -A main worker --loglevel=info -Ofair