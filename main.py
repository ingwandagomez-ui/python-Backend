from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from auth import m_hash_password, create_access_token, verfy_the_password

#  cd "C:\Users\Wanda Gómez Mirabal\Python-course by mouredev\myapi"
# and
# py -m uvicorn main:app --reload

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class User(BaseModel):
    m_name: str
    m_age: int

@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/about")
def about():
    return {"message": "Hello algorithm this is my first API"}

@app.get("/users")
def users():
    return {"users": ["Adam", "Enmanuel", "Edgar"]}

@app.post("/create-user")
def create_a_user(user: User, db: Session = Depends(get_db)):
    db_user = models.User(m_name=user.m_name, m_age=user.m_age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": f"User {user.m_name} created", "id": db_user.id}

@app.delete("/delete-user/{m_user_id}")
def m_delete_user(m_user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == m_user_id).first()
    if not user:
        return {"message": "This is not found!"}
    db.delete(user)
    db.commit()
    return {"message": f"User {m_user_id} deleted!"}

@app.put("/update-user/{m_user_id}")
def m_update_user(m_user_id: int, user: User, db: Session = Depends(get_db)):
    m_db_user = db.query(models.User).filter(models.User.id == m_user_id).first()
    if not m_db_user:
        return {"message": "This is not found"}
    m_db_user.m_name = user.m_name 
    m_db_user.m_age = user.m_age
    db.commit()
    return {"message": f"User {m_user_id} updated!!"}

class UserRegister(BaseModel):
    m_name: str
    m_age: int
    password: str

@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    hashed = m_hash_password(user.password)
    db_user = models.User(m_name=user.m_name, m_age=user.m_age, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully!", "id": db_user.id}

@app.post("/login")
def login(user: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.m_name == user.m_name).first()
    if not db_user:
        return {"message": "User not found!"}
    if not verfy_the_password(user.password, db_user.password):
        return {"message": "Wrong password!"}
    token = create_access_token(data={"sub": db_user.m_name})
    return {"access_token": token, "token_type": "bearer"}