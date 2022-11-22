from sqlalchemy import Column, Integer, String, null
from database import Base

class Animals(Base):
    __tablename__ = 'Animals'
    id = Column(Integer, primary_key=True)
    nome = Column(String(256))
    idade = Column(Integer)