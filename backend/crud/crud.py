from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, gold=1000, gems=50)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_total_heroes_available(db: Session):
    # Simula il numero totale di eroi disponibili nel gioco (usa una tabella reale se vuoi)
    return 18

def get_user_heroes(db: Session, user_id: int):
    return db.query(models.UserHero).filter(models.UserHero.user_id == user_id).all()

def add_hero_to_user(db: Session, user_id: int, hero_id: int):
    owned = db.query(models.UserHero).filter(models.UserHero.user_id == user_id).count()
    max_heroes = get_total_heroes_available(db)
    if owned >= max_heroes:
        return None
    hero = models.UserHero(user_id=user_id, hero_id=hero_id)
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero

def summon_hero(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user.gems < 5:
        return None
    from random import randint
    hero_id = randint(1, get_total_heroes_available(db))
    new_hero = add_hero_to_user(db, user_id, hero_id)
    if not new_hero:
        return "inventory_full"
    user.gems -= 5
    db.commit()
    return new_hero
