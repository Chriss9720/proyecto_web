from fastapi import APIRouter, Depends, Request

from schemas.piloto import PilotoRequest, Get

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/piloto",
    tags=["Piloto"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
async def crear(request: Request, item: PilotoRequest):
    return {"msg": "Registro exitoso"}

@router.put("/{id}")
async def actualizar(request: Request, id: int, item: PilotoRequest):
    return {"msg": "Actualizacion exitosa"}

@router.delete("/{id}")
async def delete(request: Request, id: int):
    return {"msg": "Baja exitosa"}

@router.get("/all", response_model=Get)
async def get_all(request: Request):
    return {}

@router.get('/name/{name}')
async def get_name(request: Request, name: str):
    return {"name": name}

@router.get('/exp/{exp}')
async def get_name(request: Request, exp: str):
    return {"exp": exp}

@router.get('/vuelos/{vuelos}')
async def get_name(request: Request, vuelos: str):
    return {"vuelos": vuelos}