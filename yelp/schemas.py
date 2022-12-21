from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    cuisine_style: str
    city: str

class Restaurant(RestaurantCreate):
    id: int

    class Config:
        orm_mode = True
