from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int | None
    username: str
    email: str