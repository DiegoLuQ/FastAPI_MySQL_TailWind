from sqlalchemy.orm import Session

from core.db.models.mod_productos import Model_Productos
from core.schemas.sc_productos import Schemas_Productos

async def add_producto(model:Schemas_Productos, db:Session):
    try:
        model_ = Model_Productos(**model.dict())

        db.add(model_)
        db.commit()
        db.refresh(model_)
        return model_
    except Exception as e:
        print(e)

async def get_productos(db:Session):
    try:
        datos = db.query(Model_Productos).all()
        return datos
    except Exception as e:
        print(e)

async def get_producto(id:int, db:Session):

    datos = db.query(Model_Productos).filter(Model_Productos.id_producto == id).first()
    return datos


async def delete_producto(id:int, db:Session):
    try:
        dato = db.query(Model_Productos).filter(Model_Productos.id_producto == id)
        dato.delete(synchronize_session = False)
        db.commit()
        return {"msg":"Producto Eliminado"}
    except Exception as e:
        print(e)

async def patch_producto(id:int, db:Session, model:Schemas_Productos):
    dato = db.query(Model_Productos).filter(Model_Productos.id_producto == id)

    if dato.first():
        dato.update(model.dict(exclude_unset = True))
        db.commit()
        return dato.first()
    else:
        return 0