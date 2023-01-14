from fastapi import APIRouter
from .v1 import base as base_v1


api_router = APIRouter()


api_router.include_router(base_v1.api_router, prefix="/v1")