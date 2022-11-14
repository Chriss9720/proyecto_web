from fastapi import APIRouter, Depends, Request

from services.asientos import AsientosService

from schemas.user import User
from schemas.boletos import Asientos, Asiento, Comprar

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/asiento",
    tags=["asientos"],
    responses={404: {"description": "Not found"}},
)

@router.put("/")
async def comprar(request: Request, item: Comprar, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AsientosService(db).comprar(item, current_user))
    return result

@router.get("/columna/{id_avion}/{columna}", response_model=Asientos)
async def get_all(request: Request, id_avion:int, columna: str, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AsientosService(db).get_by_columna(id_avion, columna))
    return result

@router.get("/info/{id_avion}/{columna}/{fila}", response_model=Asiento)
async def get_all(request: Request, id_avion:int, columna: str, fila: str, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AsientosService(db).get_by_fila(id_avion, columna, fila))
    return result