#!/usr/bin/env python
import logging

import aioredis
import uvicorn as uvicorn
from fastapi import FastAPI

from api.v1 import account
from core import config
from core.logger import LOGGING
from db import redis

app = FastAPI(
    title="Read-only API for Tron",
    description="Get information about account",
    version="1.0.0",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)


@app.on_event("startup")
async def startup():
    redis.redis = await aioredis.create_redis_pool(
        (config.REDIS_HOST, config.REDIS_PORT), minsize=10, maxsize=20
    )


@app.on_event("shutdown")
async def shutdown():
    await redis.redis.close()


app.include_router(account.router, prefix="/v1/balances", tags=["account"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
