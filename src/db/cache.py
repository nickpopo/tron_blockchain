import abc
from typing import List, Optional

from aioredis import Redis
from core import config

import db.redis as redis


class Cache(abc.ABC):
    @property
    @abc.abstractmethod
    def client(self):
        pass

    @abc.abstractmethod
    async def get(self):
        pass

    @abc.abstractmethod
    async def put(self):
        pass


class RedisCache(Cache):
    @property
    def client(self) -> Redis:
        return redis.redis

    async def get(self, key: str) -> Optional:
        data = await self.client.get(key)
        if not data:
            return None

        return data

    async def put(self, key: str, value):
        await self.client.set(key, value.json(), expire=config.CACHE_EXPIRE_IN_SECONDS)

    async def mget(self, keys):
        data = await self.client.mget(*keys)
        return data
