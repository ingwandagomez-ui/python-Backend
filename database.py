from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os 

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./myapi.db")

# Fix for Railway PostgreSQL URL
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()