from pydantic import BaseModel

class Checkout(BaseModel):
    checkout_id: str
    status: str 
    subtotal: float
    tax: float
    total: float 
