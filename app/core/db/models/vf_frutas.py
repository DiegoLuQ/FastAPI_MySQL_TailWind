from sqlalchemy import Column, String, DECIMAL, Integer, Date, ForeignKey
from ..base_class import Base
from sqlalchemy.orm import relationship

class Model_VF_Frutas(Base):
    __tablename__ = "vf_frutas"
    id_fruta = Column(Integer, primary_key=True)
    frut_nombre = Column(String(30), nullable=False)
    frut_peso = Column(DECIMAL(5,2), nullable = False)
    frut_stock = Column(Integer, nullable = False)
    frut_pventa = Column(Integer, nullable = False)
    frut_pcosto = Column(Integer, nullable = False)
    frut_fecha = Column(Date, nullable = False)
    id_proveedor = Column(Integer, nullable = False)