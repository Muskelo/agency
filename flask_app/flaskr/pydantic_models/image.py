from pydantic import BaseModel
from typing import Optional, List


class DumpImage(BaseModel):
    class Model(BaseModel):
        id: int
        filename: str
        user_id: int
        item_id: Optional[int]

        class Config:
            orm_mode=True

    data: Model
class DumpImagesList(BaseModel):
    class Model(BaseModel):
        id: int
        filename: str
        user_id: int
        item_id: Optional[int]

        class Config:
            orm_mode=True

    data: List[Model]
