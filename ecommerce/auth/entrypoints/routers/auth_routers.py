from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from entrypoints.schemas.auth_schema import Login, AuthToken
import httpx
from datetime import timedelta
from core.security.security import create_access_token, verify_password
import pika

router = APIRouter()

USER_SERVICE_URL = "http://users:8001/api/v1/user"


def send_login_message(username):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='login_queue')

    channel.basic_publish(exchange='',
                          routing_key='login_queue',
                          body=f'User {username} logged in')
    print(f" [x] Sent 'User {username} logged in'")
    connection.close()

#     return response
@router.post("/login", response_model=AuthToken, status_code=status.HTTP_200_OK)
async def login(login: Login):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{USER_SERVICE_URL}/{login.username}")
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail="User not found")


        user_data = response.json()
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="user not found"
            )
        else:
            if not verify_password(login.password, user_data["password"]):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail= "Password incorrecta"
                )
            
        access_token = create_access_token(data={"sub": user_data["username"]})
        # Enviar mensaje a RabbitMQ
        # send_login_message(user_data["username"])

        return AuthToken(access_token=access_token, token_type="bearer")

