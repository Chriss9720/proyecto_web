from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, Integer
from configs.database import Base

class PilotoDB(Base):
    __tablename__ = "piloto"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre_completo = Column(String(255))
    edad = Column(Integer)
    experiencia = Column(String(255))
    total_vuelos = Column(Integer)

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)