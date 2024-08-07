# app/entrypoints/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str



class UserRead(UserBase):
    id: int

class Login(BaseModel):
    username:str
    password:str