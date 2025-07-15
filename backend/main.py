from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import models
from schemas import schemas
from crud import crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserBase)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/summon/{user_id}")
def summon(user_id: int, db: Session = Depends(get_db)):
    result = crud.summon_hero(db, user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Not enough gems")
    elif result == "inventory_full":
        raise HTTPException(status_code=400, detail="Hero inventory full")
    return {"message": "Hero summoned!", "hero_id": result.hero_id}
