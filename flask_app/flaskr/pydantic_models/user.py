from pydantic import BaseModel


class CreateUser(BaseModel):
    class Model(BaseModel):
        login: str
        password: str
        number: str

    data: Model

class DumpUser(BaseModel):
    class Model(BaseModel):
        id: int
        login: str
        number: str

        class Config:
            orm_mode = True

    data: Model
