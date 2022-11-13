from pydantic import BaseModel, constr
from typing import List

from utils.regex import Regex

class PilotoRequest(BaseModel):
    nombre: str
    edad: constr(strict=True, regex=Regex.digits, min_length=1, max_length=3)
    experiencia: str
    total_vuelos: int

    def to_dict():
        return {
            "nombre": "str",
            "edad": "str",
            "experiencia": "str",
            "total_vuelos": 0
        }

class GetPiloto(PilotoRequest):
    id: int

    def to_dict():
        return {
            "id": 0,
            "nombre": "str",
            "edad": "str",
            "experiencia": "str",
            "total_vuelos": 0
        }
    
class Get(BaseModel):
    pilotos: List[GetPiloto]