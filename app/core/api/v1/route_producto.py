from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from core.db.session import get_db
from core.schemas.sc_productos import Schemas_Productos
from core.db.repository import repo_productos


router = APIRouter()

@router.post('/agregar')
async def agregar_productos(model:Schemas_Productos, db:Session=Depends(get_db)) -> Schemas_Productos:
    fruta = await repo_productos.add_producto(model=model, db=db)
    return fruta

    
@router.get('/listar')
async def listar_productos(db:Session=Depends(get_db)):
    datos = await repo_productos.get_productos(db=db)
    return datos