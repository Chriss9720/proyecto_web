from pydantic import BaseModel
from typing import List

class Pais(BaseModel):
    id: int
    code: str
    name: str

class Paises(BaseModel):
    paises: List[Pais]
    
class Estados(BaseModel):
    estados: List[Pais]