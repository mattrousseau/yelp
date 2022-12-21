from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from yelp import schemas, models
from yelp.database import SessionLocal

app = FastAPI()

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
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).all()

@app.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    db.delete(db_restaurant)
    db.commit()
    return {}

@app.post("/restaurants", response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    new_restaurant = models.Restaurant(**restaurant.dict())
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant
