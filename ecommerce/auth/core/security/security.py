from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from dotenv import load_dotenv
import os
import pytz
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


load_dotenv()



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES =1600
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_access_token(data: dict, ):
    to_encode = data.copy()
    colombia_tz = pytz.timezone("America/Bogota")
    expire = datetime.now(colombia_tz) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload
     
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


def hash_password(password:str):
    return pwd_context.hash(password)
    

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)
