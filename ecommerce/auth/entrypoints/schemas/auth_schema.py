# app/entrypoints/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime




class AuthToken(BaseModel):
    access_token: str
    token_type:str


class Login(BaseModel):
    username:str 
    password:str
    