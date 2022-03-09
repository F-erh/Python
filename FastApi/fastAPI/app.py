from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Papel(BaseModel):
    id: int
    des: str
    valor: float

app = FastAPI()

banco_de_dados = []

@app.post("/papeis")
def add_papel(papel: Papel):
    banco_de_dados.append(papel)
    return papel

@app.get("/papeis")
def list_papel():
    return banco_de_dados

@app.get("/papeis/valor-total")
def get_valor_total():
    valor_total = sum([papel.valor * papel.quantidade for papel in banco_de_dados])

    return {"valor_total": valor_total}