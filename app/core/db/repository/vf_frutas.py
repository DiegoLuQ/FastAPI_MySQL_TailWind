from sqlalchemy.orm import Session

from core.db.models.vf_frutas import Model_VF_Frutas
from core.schemas.vf_frutas import Schemas_Frutas

async def add_fruta(model:Schemas_Frutas, db:Session):
    model_ = Model_VF_Frutas(**model.dict())

    db.add(model_)
    db.commit()
    db.refresh(model_)
    return model_

async def get_frutas(db:Session):
    datos = db.query(Model_VF_Frutas).all()
    return datos

