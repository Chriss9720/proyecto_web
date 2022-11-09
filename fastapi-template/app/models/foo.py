from sqlalchemy import Boolean, Column, Integer, String

from configs.database import Base

#Modelo de la base de datos
class FooItem(Base):
    #Nombre de la tabla
    __tablename__ = "foo_items"

    #Campos de la tabla
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    public = Column(Boolean, default=False)

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)