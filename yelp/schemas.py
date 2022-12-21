from pydantic import BaseModel

class Restaurant(BaseModel):
    name: str  # list, dict, datetime, int, float, bool
    cuisine_style: str
    city: str
