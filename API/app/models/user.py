from sqlalchemy import BigInteger, Column, String, Boolean, DateTime, Integer, JSON
from sqlalchemy.sql import func
from configs.database import Base

class UsersDB(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True, index=True)
    password = Column(String(128))
    username = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(254))
    rfc = Column(String(255))
    curp = Column(String(255))
    tipo_usuario_id = Column(BigInteger)
    deleted = Column(DateTime, default = None)
    is_active = Column(Boolean, default=False)

    created_by_id = Column(BigInteger,default=1)
    created_at = Column(DateTime, default=func.now())
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

class TipoUsuarioDB(Base):
    __tablename__ = 'cs_tipo_usuario'
    id = Column(BigInteger, primary_key=True, index=True)
    tipo_usuario = Column(String(255))

    tipo_aduana_id = Column(BigInteger)

    deleted = Column(DateTime, default=None)
    deleted_by_cascade = Column(Boolean, default=False)
    created_by_id = Column(BigInteger, default=1)
    created_at = Column(DateTime, default=func.now())
    updated_by_id = Column(BigInteger, default=None)
    updated_at = Column(DateTime, onupdate=func.now())
    
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)