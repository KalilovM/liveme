FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/liveme_django

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN apk add --no-cache --virtual python-tk tk-dev
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/liveme_django/entrypoint.sh
RUN chmod +x /usr/src/liveme_django/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/liveme_django/entrypoint.sh"]

# I should run it manually
# docker compose exec web python manage.py flush --no-input
# docker compose exec web python manage.py migrate