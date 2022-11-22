from pydantic import BaseModel

class Papel(BaseModel):
    id: int
    des: str
    valor: float
