from fastapi import APIRouter

from neoh_backend.api.v1.endpoints import items

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["Items"])
