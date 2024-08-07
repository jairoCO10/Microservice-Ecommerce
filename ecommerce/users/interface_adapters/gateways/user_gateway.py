# app/interface_adapters/gateways/db_gateway.py
from typing import List
from sqlalchemy.orm import Session
from core.entities.user_entities import CreateUser, Users
from infrastructure.services.user_services import UserRepository






class UserGateway:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = UserRepository(self.db_session)

        
    async def create_user(self,  email: str, username:str, password:str,) -> CreateUser:
        orm_user = await self.repository.create_user( email, username,  password)
        return CreateUser(id=orm_user.id, email=orm_user.email, username= orm_user.username, 
                        password=orm_user.hashed_password)
    

    async def get_users(self) -> List[Users]:
        orm_users = await self.repository.get_users()
        users = []
        for orm_user in orm_users:
            users.append(Users(id=orm_user.id, 
                         username= orm_user.username,
                         email=orm_user.email,
                         password=orm_user.hashed_password))
        return users
    
    async def get_user(self, user_id: str) -> Users:
        orm_user = await self.repository.get_user(user_id)
        if orm_user:
            return Users(id=orm_user.id, 
                         username= orm_user.username,
                         email=orm_user.email,
                         password=orm_user.hashed_password )
        return None
    