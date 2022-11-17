from fastapi import APIRouter, Depends, Request

from services.aereoPuerto import AereoPuertoService

from schemas.user import User
from schemas.aereoPuerto import PostAereoPuerto, AereoPuertos

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/aereoPuerto",
    tags=["aereoPuerto"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create(request: Request, item: PostAereoPuerto, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).crear(item))
    return result

@router.put("/{id}")
async def update(request: Request, id: int, item: PostAereoPuerto, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).actualizar(id, item))
    return result

@router.delete("/{id}")
async def delete(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).deleted(id))
    return result

@router.get("/all", response_model=AereoPuertos)
async def get_all(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).get_all())
    return result

@router.get("/id/{id}", response_model=AereoPuertos)
async def get_all(request: Request, id:int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).get_by_id(id))
    return result

@router.get("/estado/{id}", response_model=AereoPuertos)
async def get_por_estado(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AereoPuertoService(db).get_by_estado(id))
    return result