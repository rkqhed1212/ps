FROM python:3
MAINTAINER Shane,Kim

RUN apt-get update && apt-get -y install \
    libpq-devvim README.md

ADD ./webpage    /app/

WORKDIR /app
CMD ["python", "manage.py", "runserver", "0:8000"]
