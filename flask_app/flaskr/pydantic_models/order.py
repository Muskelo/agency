import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class _User(BaseModel):
    id: int
    login: str
    number: str

    class Config:
        orm_mode = True


class _Image(BaseModel):
    id: int
    filename: str

    class Config:
        orm_mode = True


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
    images: List[_Image]

    class Config:
        orm_mode = True


class CreateOrder(BaseModel):
    class Model(BaseModel):
        item_id: int

    data: Model


class PatchOrder(BaseModel):
    class Model(BaseModel):
        status: Optional[str]
        comment: Optional[str]

    data: Model


class _Order(BaseModel):
    id: int
    created: datetime.datetime
    status: str
    user: _User
    item: _Item
    comment: Optional[str]

    @validator('created')
    def validate_created(cls, v):
        return v.isoformat()

    class Config:
        orm_mode = True


class DumpOrdersList(BaseModel):
    data: List[_Order]
    total: int


class DumpOrder(BaseModel):
    data: _Order
