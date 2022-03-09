from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "animals"

@app.post("/animals", response_model=schemas.Animals, status_code=status.HTTP_201_CREATED)
def create_animals(animals: schemas.AnimalsCreate, session: Session = Depends(get_session)):

    animalsdb = models.Animals(nome = animals.nome, idade = animals.idade)

    session.add(animalsdb)
    session.commit()
    session.refresh(animalsdb)

    return animalsdb

@app.get("/animals/{id}", response_model=schemas.Animals)
def read_animals(id: int, session: Session = Depends(get_session)):

    animals = session.query(models.Animals).get(id)

    if not animals:
        raise HTTPException(status_code=404, detail=f"animals item with id {id} not found")

    return animals

@app.put("/animals/{id}", response_model=schemas.Animals)
def update_animals(id: int, nome: str, idade: int, session: Session = Depends(get_session)):

    animals = session.query(models.Animals).get(id)

    if animals:
        animals.nome = nome
        animals.idade = idade
        session.commit()

    if not animals:
        raise HTTPException(status_code=404, detail=f"animals item with id {id} not found")

    return animals

@app.delete("/animals/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animals(id: int, session: Session = Depends(get_session)):

    animals = session.query(models.Animals).get(id)

    if animals:
        session.delete(animals)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"animals item with id {id} not found")

    return None

@app.get("/animals", response_model = List[schemas.Animals])
def read_animals_list(session: Session = Depends(get_session)):

    animals_list = session.query(models.Animals).all()

    return animals_list