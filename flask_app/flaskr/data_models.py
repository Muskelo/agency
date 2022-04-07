""" Module include pydantic models """

from typing import List, Optional
from pydantic import BaseModel


class BaseDumpUser(BaseModel):
    id: int
    login: str
    email: str
    roles_id: List[int]

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

class BaseLoadOptionalUser(BaseModel):
    login: Optional[str]
    email: Optional[str]
    password: Optional[str]

class LoadOptionalUser(BaseModel):
    user: BaseLoadOptionalUser


class BaseDumpRole(BaseModel):
    id: int
    name: str
    users_id: List[int]

    class Config:
        orm_mode = True

class DumpRole(BaseModel):
    role: BaseDumpRole

class DumpRoles(BaseModel):
    roles: List[BaseDumpRole]

