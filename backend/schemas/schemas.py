from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str

class UserBase(BaseModel):
    id: int
    name: str
    gold: int
    gems: int
    class Config:
        orm_mode = True

class HeroCreate(BaseModel):
    user_id: int
    hero_id: int

class ItemCreate(BaseModel):
    user_id: int
    item_name: str
    quantity: int
