from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define the Product schema
class Product(BaseModel):
    barcode: str
    name: str
    category: str
    purchase_count: int = 0

# Mock database
mock_db = {}

# MongoDB connection setup
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27018"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.grocery_app
products_collection = db.get_collection("products_collection")

@app.post("/scan/{barcode}")
async def scan_barcode(barcode: str):
    # Check if the product exists in MongoDB
    product = await products_collection.find_one({"barcode": barcode})
    if product:
        return Product(**product) if product else None
    else:
        # Save the mock product to MongoDB if not found
        mock_product = Product(
            barcode=barcode,
            name="Mock Product",
            category="Unknown",
            purchase_count=0
        )
        await products_collection.insert_one(mock_product.dict())
        return mock_product