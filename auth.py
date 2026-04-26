from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "adamemil23"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50

m_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def m_hash_password(password: str):
    return m_pwd_context.hash(password)

def verfy_the_password(plain_password, hashed_password):
    return m_pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": token_expires})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)