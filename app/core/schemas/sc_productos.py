from pydantic import BaseModel

from datetime import date

class Schemas_Productos(BaseModel):
    prod_nombre: str = None
    prod_peso: float = None
    prod_pventa: int = None
    prod_pcosto: int = None
    prod_fecha: date = None
    id_proveedor: int = None
    prod_stock: int = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "prod_nombre":"Mango",
                "prod_peso":"0.350",
                "prod_pventa":"1200",
                "prod_pcosto":"850",
                "prod_stock":95,
                "prod_fecha":"2023-01-10",
                "id_proveedor":"1"
            }
        }