from dataclasses import dataclass


@dataclass
class Users:
    id: int
    username: str
    email: str
    password: str


@dataclass
class CreateUser:
    id: str
    username: str
    email: str
    password: str


@dataclass
class AuthToken:
    access_token: str
    token_type: str

