FROM python:3.9-alpine

EXPOSE 8000

RUN mkdir -p /usr/local/var/log/gunicorn/

WORKDIR /opt/app

RUN pip install --upgrade pip

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh .
COPY ./src .

RUN chmod 441 ./docker-entrypoint.sh

CMD [ "./docker-entrypoint.sh" ]
