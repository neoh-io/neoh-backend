from typing import Optional

from pydantic import BaseModel


# Shared Properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class ItemInDB(ItemBase):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDB):
    pass
