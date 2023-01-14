from pydantic import BaseModel

from datetime import date

class Schemas_Frutas(BaseModel):
    frut_nombre: str = None
    frut_peso: float = None
    frut_pventa: int = None
    frut_pcosto: int = None
    frut_fecha: date = None
    id_proveedor: int = None
    frut_stock: int = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "frut_nombre":"Mango",
                "frut_peso":"0.350",
                "frut_pventa":"1200",
                "frut_pcosto":"850",
                "frut_stock":95,
                "frut_fecha":"2023-01-10",
                "id_proveedor":"1"
            }
        }