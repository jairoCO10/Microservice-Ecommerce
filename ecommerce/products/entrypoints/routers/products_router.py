from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from interface_adapters.gateways.user_gateway import UserGateway
# from core.usecases.user_usecases import UserUseCase
# from entrypoints.schemas.user_schemas import  UserCreate, UserRead
from infrastructure.database import Connect
# from interface_adapters.dependencies.jwt import get_current_user


router = APIRouter()


@router.get("/products")
async def list_products(db:Session = Depends(Connect.get_db)):
    '''
    
    '''
    pass