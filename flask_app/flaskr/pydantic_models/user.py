from typing import List, Optional
from pydantic import BaseModel


class CreateUser(BaseModel):
    class Model(BaseModel):
        login: str
        password: str
        number: str

    data: Model


class PatchUser(BaseModel):
    class Model(BaseModel):
        role: Optional[str]

    data: Model


class DumpUser(BaseModel):
    class Model(BaseModel):
        id: int
        login: str
        number: str

        class Config:
            orm_mode = True

    data: Model

class _User(BaseModel):
    id: int
    login: str
    number: str
    role: Optional[str]

    class Config:
        orm_mode = True

class DumpCurrentUser(BaseModel):
    data: _User

class DumpUsersList(BaseModel):
    data: List[_User]
    total: int
