from fastapi import FastAPI
from uuid import UUID, uuid4
import json
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my checkout API!"}

class Checkout(BaseModel):
    checkout_id: str
    status: str 
    subtotal: float
    tax: float
    total: float 


# Create a new checkout and return the checkout object
@app.post("/checkout")
def create_checkout():
    c = Checkout(checkout_id=str(uuid4()), status="payment_pending", subtotal=0.0, tax=0.0, total=0.0)
    return(c.model_dump())



