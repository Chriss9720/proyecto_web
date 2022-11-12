from fastapi import APIRouter, Depends, Request

from schemas.paises_estados import Paises, Estados

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/paisEstado",
    tags=["paisEstados"],
    responses={404: {"description": "Not found"}},
)

@router.get("/paises", response_model=Paises)
async def paises(request: Request):
    return {"msg": "Registro exitoso"}

@router.get("/estados/{id}", response_model=Estados)
async def paises(request: Request, id: int):
    return {"msg": "Registro exitoso"}