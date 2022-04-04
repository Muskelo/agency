""" Module include pydantic models """

from typing import List
from pydantic import BaseModel

class BaseDumpUser(BaseModel):
    id: int
    login: str
    email: str

    class Config:
        orm_mode = True

class DumpUser(BaseModel):
    user: BaseDumpUser

class DumpUsers(BaseModel):
    users: List[BaseDumpUser]

class BaseLoadUser(BaseModel):
    login: str
    email: str
    password: str

class LoadUser(BaseModel):
    user: BaseLoadUser
