from pydantic import BaseModel, constr
from typing import List

from utils.regex import Regex

from datetime import datetime

class Escala(BaseModel):
    aereoPuerto: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)
    salida: datetime
    llegada: datetime

class Escalas(BaseModel):
    escalas: List[Escala]

class PostAvion(BaseModel):
    cap_max_pasajeros: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)
    cap_max_equipaje_kilos: constr(strict=True, regex=Regex.floats, max_length=255, min_length=1)
    origen_id: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)
    destino_id: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)
    escalas: List[Escala]
    salida: datetime
    llegada: datetime
    filas: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)
    estado: str
    piloto_id: constr(strict=True, regex=Regex.digits, max_length=255, min_length=1)

class Avion(PostAvion):
    id: int
    folio: str

class GetAvion(BaseModel):
    aviones: List[Avion]