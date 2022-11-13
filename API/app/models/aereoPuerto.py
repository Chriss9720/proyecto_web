from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey
from configs.database import Base

from models.ciudad import CiudadDB

class AereoPuertoDB(Base):
    __tablename__ = "aereoPuerto"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String(255))
    direccion = Column(String(255))
    codigo_postal = Column(String(255))
    ciudad_id = Column(BigInteger, ForeignKey(f"{CiudadDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)