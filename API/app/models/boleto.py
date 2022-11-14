from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func

from configs.database import Base

from models.user import UsersDB
from models.asiento import AsientoDB

class BoletoDB(Base):
    __tablename__ = "boleto"

    id = Column(BigInteger, primary_key=True, index=True)
    folio = Column(String(14))
    fecha_hora_compra = Column(DateTime, default=func.now())
    sub_total = Column(Float)
    iva = Column(Float, default=1.22)
    total = Column(Float)

    asiento_id = Column(BigInteger, ForeignKey(f"{AsientoDB.__tablename__}.id"))
    usuario_id = Column(BigInteger, ForeignKey(f"{UsersDB.__tablename__}.id"))

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)