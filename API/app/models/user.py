from sqlalchemy import BigInteger, Column, String, Boolean, DateTime
from configs.database import Base

class UsersDB(Base):
    __tablename__ = "usuario"
    id = Column(BigInteger, primary_key=True, index=True)

    nombre = Column(String(255))
    apellido_paterno = Column(String(255))
    apellido_materno = Column(String(255))
    correo = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))
    empleado = Column(String(255))
    
    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)