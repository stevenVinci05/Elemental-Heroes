from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine
from database import SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency per DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/add_hero", response_model=schemas.InventoryItem)
def add_hero(user_id: str, hero: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    try:
        return crud.add_hero_to_inventory(db, user_id, hero)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
