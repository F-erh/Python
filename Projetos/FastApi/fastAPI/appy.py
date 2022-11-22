import databases
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
from pydal import DAL, Field
from datetime import datetime

from pydantic import BaseModel

from config import config
from services.product import Product as product_service


class Product (BaseModel):

    id: int
    name: str
    sku: str


class Payload (BaseModel):

    deleted: List[str]
    updated: List[Product]


db = DAL(config.DB_URI)
product = db.define_table('product',
                          Field('name', 'string'),
                          Field('sku', 'string'),
                          Field('last_update', 'datetime'),
                          Field('deleted', 'boolean'))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sync")
def sync(reference: Optional[datetime] = None):
    product_svc = product_service(db)
    return product_svc.get_status(reference)


@app.post("/sync")
def update(products: Payload):
    product_svc = product_service(db)
    return product_svc.update(products.dict())


product_svc = product_service(db)
product_svc.compare()

@app.get("/product/list")
def list_product():
    return db

@app.post("/product/add")
async def add_product(pr: Product):
    query=db.insert().values(
        name=pr.name,
        sku=pr.sku
    )
    await databases.execute(query)
    return {"adcionado com sucesso"}

@app.put('/product/update/{product_id}')
async def update_product(id: int, pr: int):
    query=db.insert().values(
        name=pr.name,
        sku=pr.sku
    )
    await databases.execute(query)
    return {"status": "updated"}

@app.delete('/product/{product_id}')
async def delete(product_id: int):
    await Product.get(id=product_id).delete()
    return {"status": "ok"}