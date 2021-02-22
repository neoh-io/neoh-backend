from .base import CRUDBase
from neoh_backend.models.item import Item
from neoh_backend.schemas.item import ItemCreate, ItemUpdate
item = CRUDBase[Item, ItemCreate, ItemUpdate]
