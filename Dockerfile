FROM python:3.10.8-alpine

WORKDIR /usr/src/cryptocoin_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./.env ./cryptocoin_app/.env
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/cryptocoin_app/entrypoint.sh
RUN chmod +x /usr/src/cryptocoin_app/entrypoint.sh
COPY . .
RUN mkdir -p /usr/src/cryptocoin_app/webapp/static