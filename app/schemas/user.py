from pydantic import BaseModel
from typing import List, Optional

# Pydantic schema for User
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic schema for listing users
class UserListResponse(BaseModel):
    users: List[User]