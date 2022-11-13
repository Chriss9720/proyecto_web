from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey, Integer, Float, Date
from configs.database import Base

from models.aereoPuerto import AereoPuertoDB
from models.piloto import PilotoDB

class AvionDB(Base):
    __tablename__ = "avion"

    id = Column(BigInteger, primary_key=True, index=True)
    folio = Column(String(14))
    cap_max_pasajeros = Column(Integer)
    cap_max_equipaje_kilos = Column(Float)
    escalas = Column(Boolean, default=False)
    salida = Column(Date)
    llegada = Column(Date)
    filas = Column(Integer)
    columnas = Column(Integer, default=4)
    estado = Column(String(255))
    destino_id_id = Column(BigInteger, ForeignKey(f"{AereoPuertoDB.__tablename__}.id"))
    origen_id_id = Column(BigInteger, ForeignKey(f"{AereoPuertoDB.__tablename__}.id"))
    piloto_id = Column(BigInteger, ForeignKey(f"{PilotoDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)