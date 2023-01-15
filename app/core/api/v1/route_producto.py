from fastapi import APIRouter, Depends
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from core.db.session import get_db
from core.schemas.sc_productos import Schemas_Productos
from core.db.repository import repo_productos
from core.helpers.message import ReponseModel

router = APIRouter()

@router.post('/agregar')
async def agregar_productos(model:Schemas_Productos, db:Session=Depends(get_db)):
    data = await repo_productos.add_producto(model=model, db=db)
    return ReponseModel(201, data, "Productos Creado")

@router.get('/listar')
async def listar_productos(db:Session=Depends(get_db)):
    datos = await repo_productos.get_productos(db=db)
    if not datos:
        return ReponseModel(404, "Productos no Encontrados", False)
    return ReponseModel(200, datos, "Listado de Productos")

@router.get('/{id}')
async def buscar_producto(id:int, db:Session=Depends(get_db)):
    dato = await repo_productos.get_producto(id=id, db=db)
    if not dato:
        return JSONResponse(status_code=404,content={"message":"No Encontrado"})
    return JSONResponse(status_code=200, content={"message":jsonable_encoder(dato)})

@router.delete('/eliminar_producto/{id}')
async def eliminar_producto(id:int, db:Session=Depends(get_db)):
    dato = await repo_productos.delete_producto(id, db)
    return dato

@router.patch('/{id}')
async def parchar_producto(id:int, model: Schemas_Productos, db:Session=Depends(get_db)):
    dato = await repo_productos.patch_producto(id, db, model)
    return ReponseModel(200, "Producto Modificado", dato)