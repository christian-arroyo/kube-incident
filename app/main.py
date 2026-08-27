
"""
The checkout API creates a checkout call to the payment service
Calculates subtotal, tax, and total for the order
Creates a checkout with payment_pending status and returns the checkout id to the client
Calls the payment service to process the payment and updates the checkout status to paid or failed
"""
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from pydantic import BaseModel

from app.core.logging import setup_logging

from app.models.checkout import Checkout

setup_logging()

checkout_data = {}

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to my checkout API!"}


# Create a new checkout and return the checkout id
@app.post("/checkout")
async def create_checkout():
    # Change this after implementing database storage for checkout data
    id = "checkout-" + str(len(checkout_data) + 1)
    c = Checkout(checkout_id=id, status="payment_pending", subtotal=0.0, tax=0.0, total=0.0)
    checkout_data[c.checkout_id] = c
    return(c.checkout_id)
    # Calculate order total
    # Call Go Payment service
    # Store checkout result
    # Return completed or failed status

# Get checkout object by ID
@app.get("/checkout/{checkout_id}")
def get_checkout(checkout_id: str):
    if checkout_id in checkout_data:
        return checkout_data[checkout_id]
    else:
        raise HTTPException(status_code=404, detail="Checkout {checkout_id} not found")
