from pydantic import BaseModel
from typing import List

from datetime import datetime

class Escalas(BaseModel):
    aereoPuerto: str
    salida: datetime
    llegada: datetime

class PostAvion(BaseModel):
    cap_max_pasajeros: int
    cap_max_equipaje_kilos: float
    origen_id: str
    destino_id: str
    escalas: List[Escalas]
    salida: datetime
    llegada: datetime
    filas: int
    estado: str
    piloto_id: str

class Avion(PostAvion):
    id: int
    folio: str

class GetAvion(BaseModel):
    aviones: List[Avion]