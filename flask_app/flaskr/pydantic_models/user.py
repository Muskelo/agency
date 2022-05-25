from typing import Optional
from pydantic import BaseModel


class CreateUser(BaseModel):
    class Model(BaseModel):
        login: str
        password: str
        number: str

    data: Model


class PatchUser(BaseModel):
    class Model(BaseModel):
        login: Optional[str]
        password: Optional[str]
        number: Optional[str]

    data: Model


class DumpUser(BaseModel):
    class Model(BaseModel):
        id: int
        login: str
        number: str

        class Config:
            orm_mode = True

    data: Model

class DumpCurrentUser(BaseModel):
    class Model(BaseModel):
        id: int
        login: str
        number: str
        role: str

        class Config:
            orm_mode = True

    data: Model
