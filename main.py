from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, crud, schema
from db import SessionLocal, engine
import horoscope

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    arbitrary_types_allowed=True
)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
async def register_user(user: schema.UserCreate, db = Depends(get_db)):
    try:
        crud.create_user(db, user)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="We are currently facing a challenge, please try again later")

@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {"users": users}

@app.get("/horoscope/{user_name}")
async def get_horoscope(user_name, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == user_name).first()
    print(user.name)
    horoscope_for_the_day = horoscope.chart(user)
    return {"horoscope": horoscope_for_the_day}
