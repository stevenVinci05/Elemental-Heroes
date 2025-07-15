from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import metadata, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    coins = Column(Integer, default=0)
    gems = Column(Integer, default=0)

class InventoryItem(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    hero_id = Column(String)
    name = Column(String)
    stars = Column(Integer)
    element = Column(String)
