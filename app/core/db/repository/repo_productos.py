from sqlalchemy.orm import Session

from core.db.models.mod_productos import Model_Productos
from core.schemas.sc_productos import Schemas_Productos

async def add_producto(model:Schemas_Productos, db:Session):
    model_ = Model_Productos(**model.dict())

    db.add(model_)
    db.commit()
    db.refresh(model_)
    return model_

async def get_productos(db:Session):
    datos = db.query(Model_Productos).all()
    return datos

