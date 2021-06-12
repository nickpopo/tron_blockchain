import datetime
import decimal
import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from services.account import AccountService, get_account_service

logger = logging.getLogger(__name__)

router = APIRouter()

# View models
class Account(BaseModel):
    address: str
    balance: decimal.Decimal
    timestamp: datetime.datetime


class Response(BaseModel):
    result: List[Account]
    not_found: List[str]
    not_valid: List[str]


class RequestBody(BaseModel):
    addresses: List[str]


@router.get("/", response_model=Response)
async def get_details(
    request_body: RequestBody,
    account_service: AccountService = Depends(get_account_service),
) -> List[Account]:

    addresses = set(request_body.dict()["addresses"])

    try:
        response = Response(**await account_service.get_all(addresses))
    except Exception as e:
        msg = "Service temporary unavailable. Try later."
        logger.exception(msg)
        raise HTTPException(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail=msg)

    return response
