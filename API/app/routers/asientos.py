from fastapi import APIRouter, Depends, Request

from schemas.boletos import Asientos, Asiento, Comprar

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/asiento",
    tags=["asientos"],
    responses={404: {"description": "Not found"}},
)

@router.put("/{id}")
async def comprar(request: Request, item: Comprar):
    return {"msg": "Registro exitoso"}

@router.get("/columna/{id_avion}/{columna}", response_model=Asientos)
async def get_all(request: Request, id_avion:int, columna: str):
    return ""

@router.get("/info/{id_avion}/{columna}/{fila}", response_model=Asiento)
async def get_all(request: Request, id_avion:int, columna: str, fila: str):
    return ""