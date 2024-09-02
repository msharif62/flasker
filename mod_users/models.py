from sqlalchemy import Column, Integer, String
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    role = Column(Integer(), nullable=False, default=0)
    full_name = Column(String(30), nullable=True, unique=False)