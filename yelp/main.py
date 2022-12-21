from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from yelp import schemas, models
from yelp.database import SessionLocal

app = FastAPI()

db = [{"name": "Chez Justine", "cuisine_style": "French", "city": "Paris"},
      {"name": "L'Alicheur", "cuisine_style": "Asian", "city": "Paris"}]

def get_db():
    """Helper function which opens a connection to the database and also manages closing the connection
    See https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/restaurants", response_model=List[schemas.Restaurant])
def get_restaurants():
    return db

@app.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
def get_restaurant(restaurant_id: int):
    return db[restaurant_id - 1]

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int):
    db.pop(restaurant_id - 1)
    return {}

@app.post("/restaurants")
def create_restaurant(restaurant: schemas.Restaurant):
    db.append(restaurant.dict())
    return db[-1]
