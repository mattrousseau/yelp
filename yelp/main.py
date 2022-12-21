from typing import List
from fastapi import FastAPI
from yelp import schemas

app = FastAPI()

db = [{"name": "Chez Justine", "cuisine_style": "French", "city": "Paris"},
      {"name": "L'Alicheur", "cuisine_style": "Asian", "city": "Paris"}]

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
