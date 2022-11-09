from pydantic import BaseModel, constr
from typing import List, Dict

#Entidades que se reciben o regresar, POST y GET
class FooItemBase(BaseModel):
    description: constr(strict=True)

class FooItemCreate(FooItemBase):
    public: bool

class FooItem(FooItemBase):
    id: int

    class Config:
        #Mapea los modelos de la base de datos
        orm_mode = True

class FooItemUpdate(FooItemCreate):
    id: int
    