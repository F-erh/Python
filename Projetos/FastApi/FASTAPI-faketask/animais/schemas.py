from pydantic import BaseModel

# Create animals Schema (Pydantic Model)
class AnimalsCreate(BaseModel):
    nome: str
    idade: int

# Complete animals Schema (Pydantic Model)
class Animals(BaseModel):
    id: int
    nome: str
    idade: int

    class Config:
        orm_mode = True