from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    m_name = Column(String)
    m_age = Column(Integer)
    password = Column(String)