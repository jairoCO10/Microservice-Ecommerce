# app/core/usecases/user_usecase.py
from typing import List
from core.entities.user_entities import Users, CreateUser
from interface_adapters.gateways.user_gateway import UserGateway

class UserUseCase:
    def __init__(self, user_gateway: UserGateway):
        self.user_gateway = user_gateway

    async def create_user(self, email: str, username:str,  password:str) -> CreateUser:
        return await self.user_gateway.create_user(email, username,  password)

    async def get_user(self, user_id: str) -> Users:
        return await self.user_gateway.get_user(user_id)
    
    async def get_users(self,) -> Users:
        return await self.user_gateway.get_users()

    async def update_user(self, user_id: int, name: str, email: str) -> Users:
        return await self.user_gateway.update_user(user_id, name, email)

    async def delete_user(self, user_id: int) -> Users:
        return await self.user_gateway.delete_user(user_id)
    