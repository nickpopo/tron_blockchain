import datetime
import decimal

from pydantic import BaseModel

# Model for business logic
class Account(BaseModel):
    address: str
    balance: decimal.Decimal
    timestamp: datetime.datetime
