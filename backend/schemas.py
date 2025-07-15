from pydantic import BaseModel
from typing import List, Optional

class InventoryItemBase(BaseModel):
    hero_id: str
    name: str
    stars: int
    element: str

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItem(InventoryItemBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    coins: int
    gems: int
    inventory: List[InventoryItem] = []

    class Config:
        orm_mode = True
