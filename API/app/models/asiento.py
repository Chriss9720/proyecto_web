from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey, Float
from configs.database import Base

from models.avion import AvionDB

class AsientoDB(Base):
    __tablename__ = "asiento"

    id = Column(BigInteger, primary_key=True, index=True)
    columna = Column(String(1))
    fila = Column(String(1))
    primera_clase = Column(Boolean, default=False)
    Asiento = Column(String(2))
    disponible = Column(Boolean, default=True)
    costo = Column(Float, default=1500.99)
    avion_id = Column(BigInteger, ForeignKey(f"{AvionDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)