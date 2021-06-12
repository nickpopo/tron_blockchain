import datetime
import logging
from asyncio import sleep
from functools import lru_cache
from http import HTTPStatus
from typing import List

import tronpy.exceptions as tronpy_exc
from core import config
from db.cache import Cache, RedisCache
from fastapi import Depends, HTTPException
from models.account import Account
from parties.party import Party, TronParty

logger = logging.getLogger(__name__)


class AccountService:
    def __init__(self, cache: Cache, party: Party):
        self.cache = cache
        self.party = party

    async def get_all(self, addresses):
        cached_obj, not_cached_addrs = await self._get_all_from_cache(addresses)

        not_found = []
        not_valid = []
        party_obj = []

        for address in not_cached_addrs:
            account = None
            try:
                account = await self._get_from_party(address)

            except tronpy_exc.BadAddress as e:
                logger.info(e.args[0])
                not_valid.append(address)

            except tronpy_exc.AddressNotFound as e:
                logger.info(e.args[0])
                not_found.append(address)

            if account:
                party_obj.append(account)
                await self._put_to_cache(account)

        return {
            "result": cached_obj + party_obj,
            "not_found": not_found,
            "not_valid": not_valid,
        }

    async def _get_from_party(self, address):
        data = await self.party.get(address)
        return Account(**data) if data else None

    async def _get_all_from_cache(self, addresses):
        addresses = list(addresses)

        data = await self.cache.mget(addresses)

        accounts = []
        not_cached_addrs = []

        for address, value in zip(addresses, data):
            if value:
                accounts.append(Account.parse_raw(value))
            else:
                not_cached_addrs.append(address)

        return accounts, not_cached_addrs

    async def _put_to_cache(self, account: Account):
        await self.cache.put(key=account.address, value=account)


@lru_cache
def get_account_service(
    cache: Cache = Depends(RedisCache), party: Party = Depends(TronParty)
) -> AccountService:
    return AccountService(cache, party)
