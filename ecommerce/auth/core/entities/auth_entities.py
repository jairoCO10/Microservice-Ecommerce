from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class AuthToken:
    access_token: str
    token_type:str