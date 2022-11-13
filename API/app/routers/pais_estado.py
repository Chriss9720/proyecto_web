from fastapi import APIRouter, Depends, Request

from services.pais_estado import PaisEstadoService

from schemas.user import User
from schemas.paises_estados import Paises, Estados

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/paisEstado",
    tags=["paisEstados"],
    responses={404: {"description": "Not found"}},
)

@router.get("/paises", response_model=Paises)
async def paises(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PaisEstadoService(db).get_paises())
    return result

@router.get("/estados/{id}", response_model=Estados)
async def paises(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PaisEstadoService(db).estado_by_pais(id))
    return result