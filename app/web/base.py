from fastapi import APIRouter
from .productos.productos import router as router_productos


web_router = APIRouter(include_in_schema=False)

web_router.include_router(router_productos, prefix="", tags=["Productos"])
