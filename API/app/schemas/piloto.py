from pydantic import BaseModel
from typing import List

class PilotoRequest(BaseModel):
    nombre: str
    edad: str
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