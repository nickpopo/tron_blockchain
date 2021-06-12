import abc
import datetime
import logging
from http import HTTPStatus
from typing import List, Optional

import backoff
import db.redis as redis
import httpx
import tronpy.exceptions as tronpy_exc
from core import config
from fastapi import HTTPException
from tronpy import AsyncTron
from tronpy.async_tron import AsyncHTTPProvider
from tronpy.defaults import conf_for_name

logger = logging.getLogger(__name__)


def backoff_hdlr(details):

    logger.info(
        "Backing off {wait:0.1f} seconds after {tries} tries "
        "calling function {target} with args {args} and kwargs "
        "{kwargs}".format(**details)
    )


class Party(abc.ABC):
    @abc.abstractmethod
    async def get(self):
        pass


class TronParty(Party):
    @backoff.on_exception(
        backoff.expo,
        (
            httpx.ConnectTimeout,
            httpx.ConnectError,
        ),
        max_time=30,
        jitter=backoff.full_jitter,
        on_backoff=backoff_hdlr,
    )
    async def get(self, address):

        async with AsyncTron(
            AsyncHTTPProvider(
                endpoint_uri=conf_for_name(config.TRON_CLIENT_NETWORK),
                timeout=config.TRON_CLIENT_TIMEOUT,
                api_key=config.TRON_CLIENT_API_KEY,
            )
        ) as client:

            balance = await client.get_account_balance(address)

            return dict(
                address=f"{address}",
                balance=balance,
                timestamp=datetime.datetime.utcnow(),
            )
