from fastapi import APIRouter, Depends, Request

from services.piloto import PilotoService

from schemas.piloto import PilotoRequest, Get
from schemas.user import User

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/piloto",
    tags=["Piloto"],
    responses={404: {"description": "Not found"}},
)

@router.post("")
async def crear(request: Request, item: PilotoRequest, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).crear(item))
    return result

@router.put("/{id}")
async def actualizar(request: Request, id: int, item: PilotoRequest, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).actualizar(id, item))
    return result

@router.delete("/{id}")
async def delete(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).deleted(id))
    return result

@router.get("/all", response_model=Get)
async def get_all(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).get_all())
    return result

@router.get('/name/{name}')
async def get_name(request: Request, name: str, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).get_by_name(name))
    return result

@router.get('/exp/{exp}')
async def get_exp(request: Request, exp: str, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).get_by_exp(exp))
    return result

@router.get('/vuelos/{vuelos}')
async def get_vuelos(request: Request, vuelos: str, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).get_by_vuelos(vuelos))
    return result

@router.get('/id/{id}')
async def get_id(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(PilotoService(db).get_by_id(id))
    return result