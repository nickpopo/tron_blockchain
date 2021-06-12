import datetime
import decimal

import orjson
from pydantic import BaseModel

# Model for business logic
class Account(BaseModel):
    address: str
    balance: decimal.Decimal
    timestamp: datetime.datetime

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson.dumps
