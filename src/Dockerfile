FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk update && apk add gcc g++ && mkdir -p /usr/local/var/log/gunicorn/

WORKDIR /opt/app

# install dependencies
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod 441 ./docker-entrypoint.sh

CMD [ "./docker-entrypoint.sh" ]
