from pydantic import BaseModel
from typing import List

class PostAereoPuerto(BaseModel):
    ciudad_id: str
    nombre: str
    direccion: str
    codigo_postal: str

class AereoPuerto(PostAereoPuerto):
    id: int

class AereoPuertos(BaseModel):
    aereo_puertos: List[AereoPuerto]