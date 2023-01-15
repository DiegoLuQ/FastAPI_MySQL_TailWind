from fastapi import APIRouter
from core.api.v1.route_producto import router as route_producto


api_router = APIRouter()


api_router.include_router(route_producto, prefix="/productos", tags=["Productos"])
