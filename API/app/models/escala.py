from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey, Float, Integer, Date
from configs.database import Base

from models.aereoPuerto import AereoPuertoDB
from models.avion import AvionDB

class AereoPuertoDB(Base):
    __tablename__ = "escala"

    id = Column(BigInteger, primary_key=True, index=True)

    salida = Column(Date)
    llegada = Column(Date)

    aereoPuerto_id = Column(BigInteger, ForeignKey(f"{AereoPuertoDB.__tablename__}.id"))
    avion_id = Column(BigInteger, ForeignKey(f"{AvionDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)