from sqlalchemy import BigInteger, Column, String, Boolean, DateTime
from configs.database import Base

class PaisDB(Base):
    __tablename__ = "pais"

    id = Column(BigInteger, primary_key=True, index=True)
    
    clave = Column(String(255))
    pais = Column(String(255))
    
    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)