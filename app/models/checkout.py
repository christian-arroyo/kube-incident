from decimal import Decimal
from enum import Enum
from pydantic import BaseModel

# Response model for checkout
class CheckoutResponseModel(BaseModel):
    checkout_id: str
    status: str 
    subtotal: Decimal
    tax: Decimal
    total: Decimal 

# Request body when creating a checkout
class CheckoutRequestModel(BaseModel):
    user_id: int
    items: list[dict]
    subtotal: Decimal
    tax_rate: Decimal

class CheckoutStatusEnum(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
