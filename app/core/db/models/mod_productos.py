from sqlalchemy import Column, String, DECIMAL, Integer, Date, ForeignKey
from ..base_class import Base
from sqlalchemy.orm import relationship

class Model_Productos(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True)
    prod_nombre = Column(String(30), nullable=False)
    prod_peso = Column(DECIMAL(5,2), nullable = False)
    prod_stock = Column(Integer, nullable = False)
    prod_pventa = Column(Integer, nullable = False)
    prod_pcosto = Column(Integer, nullable = False)
    prod_fecha = Column(Date, nullable = False)
    id_proveedor = Column(Integer, nullable = False)