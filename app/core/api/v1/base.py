from fastapi import APIRouter
from core.api.v1.route_fruta import router as route_fruta


api_router = APIRouter()


api_router.include_router(route_fruta, prefix="/fruta", tags=["Frutas"])
