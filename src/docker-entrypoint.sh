#!/bin/sh
export `cat .env_local`
gunicorn main:app --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
exec "$@"