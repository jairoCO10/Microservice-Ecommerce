# auth_service/app/models.py
from sqlalchemy import Column, Integer, String
from infrastructure.database import Connection

class User(Connection.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)