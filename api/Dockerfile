FROM python:3.8.1-alpine3.11

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 5001
ENV DEBUG true

COPY . /usr/src/app
WORKDIR /usr/src/app

# install requirements
RUN pip install --no-cache-dir  -r requirements.txt

# expose the app port
EXPOSE 5001

RUN pip install gunicorn

# run the app server
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "5", "app:app"]