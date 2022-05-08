import datetime
from typing import List

from pydantic import BaseModel, validator


class CreateOrder(BaseModel):
    class Model(BaseModel):
        item_id: int

    data: Model

class PatchOrder(BaseModel):
    class Model(BaseModel):
        status: str

    data: Model

class _User(BaseModel):
    id: int
    login: str
    number: str

    class Config:
        orm_mode = True


class DumpOrder(BaseModel):
    class Model(BaseModel):
        id: int
        created: datetime.datetime
        status: str
        user: _User

        @validator('created')
        def validate_created(cls, v):
            return v.isoformat()

        class Config:
            orm_mode = True

    data: Model


class DumpOrdersListForItem(BaseModel):
    class Model(BaseModel):
        id: int
        created: datetime.datetime
        status: str
        user: _User

        @validator('created')
        def validate_created(cls, v):
            return v.isoformat()

        class Config:
            orm_mode = True

    data: List[Model]


class _Item(BaseModel):
    id: int
    size: int
    price: int
    rooms: int
    floor: int
    total_floor: int
    type: str
    city: str
    address: str
    description: str
    images_id: List[int]

    class Config:
        orm_mode = True


class DumpOrdersListForUser(BaseModel):
    class Model(BaseModel):
        id: int
        created: datetime.datetime
        status: str
        item: _Item

        @validator('created')
        def validate_created(cls, v):
            return v.isoformat()

        class Config:
            orm_mode = True

    data: List[Model]
