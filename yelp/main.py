from fastapi import FastAPI

app = FastAPI()

db = [{"name": "Chez Justine", "cuisine_style": "French", "city": "Paris"},
      {"name": "L'Alicheur", "cuisine_style": "Asian", "city": "Paris"}]

@app.get("/restaurants")
def get_restaurants():
    return db

@app.get("/restaurants/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    return db[restaurant_id - 1]

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int):
    db.pop(restaurant_id - 1)
    return {}
