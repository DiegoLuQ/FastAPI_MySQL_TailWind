from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from core.db.session import get_db
from core.schemas.vf_frutas import Schemas_Frutas
from core.db.repository import vf_frutas


router = APIRouter()

@router.post('/agregar')
async def agregar_frutas(model:Schemas_Frutas, db:Session=Depends(get_db)) -> Schemas_Frutas:
    fruta = await vf_frutas.add_fruta(model=model, db=db)
    return fruta

    
@router.get('/frutas')
async def listar_frutas(db:Session=Depends(get_db)):
    datos = await vf_frutas.get_frutas(db=db)
    return datos