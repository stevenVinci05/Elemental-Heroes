import uuid
from sqlalchemy.orm import Session
from models import User, InventoryItem
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(id=str(uuid.uuid4()), username=user.username, coins=0, gems=0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def add_hero_to_inventory(db: Session, user_id: str, hero: schemas.InventoryItemCreate):
    inventory_count = db.query(InventoryItem).filter(InventoryItem.user_id == user_id).count()
    if inventory_count >= 1000:
        raise Exception("Inventory full")
    db_hero = InventoryItem(user_id=user_id, **hero.dict())
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero
