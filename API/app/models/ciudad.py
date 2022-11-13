from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey
from configs.database import Base

from models.pais import PaisDB

class CiudadDB(Base):
    __tablename__ = "ciudad"

    id = Column(BigInteger, primary_key=True, index=True)
    
    clave = Column(String(255))
    ciudad = Column(String(255))
    
    pais_id = Column(BigInteger, ForeignKey(f"{PaisDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)