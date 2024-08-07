from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from entrypoints.schemas.auth_schema import Login
from core.entities.auth_entities import AuthToken



class AuthController:
    def __init__(self, db:Session) -> None:
        self.connection = db
        self.mensaje_token_vencido = "token vencido"
        self.authservice = AuthService(db)
       


    async def auth_login(self, users:Login)->AuthToken:
        
       

        if not data_login:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="user not found"
            )
        else:
            if not jwt.verify_password(users.password, data_login.password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail= "Password incorrecta"
                )
        data = {
            "usuario": data_login.users,
            "nombre": data_login.name,
        }
       
        access_token = jwt.create_access_token(data=data)
        return AuthToken(access_token=access_token, token_type="bearer")