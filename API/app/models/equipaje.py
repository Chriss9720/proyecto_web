from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey, Float, Integer
from configs.database import Base

from models.asiento import AsientoDB

class AereoPuertoDB(Base):
    __tablename__ = "equipaje"

    id = Column(BigInteger, primary_key=True, index=True)

    peso_total = Column(Float)
    costo_extra = Column(Float)
    consecutivo = Column(Integer)

    asiento_id = Column(BigInteger, ForeignKey(f"{AsientoDB.__tablename__}".id))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)