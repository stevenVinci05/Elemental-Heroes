from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    gold = Column(Integer, default=0)
    gems = Column(Integer, default=0)

    heroes = relationship("UserHero", back_populates="owner")
    items = relationship("UserItem", back_populates="owner")

class UserHero(Base):
    __tablename__ = "user_heroes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hero_id = Column(Integer)

    owner = relationship("User", back_populates="heroes")

class UserItem(Base):
    __tablename__ = "user_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_name = Column(String)
    quantity = Column(Integer, default=1)

    owner = relationship("User", back_populates="items")
