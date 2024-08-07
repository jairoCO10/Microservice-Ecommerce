# auth_service/app/main.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from interface_adapters.gateways.user_gateway import UserGateway
from core.usecases.user_usecases import UserUseCase
from entrypoints.schemas.user_schemas import  UserCreate, UserRead
from infrastructure.database import Connect
from interface_adapters.dependencies.jwt import get_current_user


router = APIRouter()


@router.post("/register/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(Connect.get_db)):
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.create_user( user.email, user.username,  user.password)


@router.get("/user/{user_id}")
async def get_user(user_id: str, db: Session = Depends(Connect.get_db)):
    # Aquí se haría la lógica para obtener el usuario de la base de datos
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)

    return await user_usecase.get_user(user_id)


@router.get("/users/")
async def get_user(db: Session = Depends(Connect.get_db), current_user: dict = Depends(get_current_user)):
    print(current_user)
    user_gateway = UserGateway(db)
    user_usecase = UserUseCase(user_gateway)
    return await user_usecase.get_users()