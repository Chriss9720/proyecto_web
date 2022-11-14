from pydantic import BaseModel
from typing import List, Optional

from datetime import date

from schemas.Avion import Escala

class PutAsiento(BaseModel):
    id: int

class Comprar(BaseModel):
    ids: List[PutAsiento]

class Asiento(BaseModel):
    fila: str
    columna: str
    primera_clase: bool
    disponible: bool
    costo: float
    id: int
    asiento: str

class Asientos(BaseModel):
    asientos: List[Asiento]

class Boleto(BaseModel):
    folio: str
    origen_id: str
    destino_id: str
    escalas: Optional[List[Escala]]
    salida: date
    llegada: date
    estado: str
    asientos: List[Asiento]

class Boletos(BaseModel):
    boletos: List[Boleto]