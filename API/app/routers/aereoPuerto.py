from fastapi import APIRouter, Depends, Request

from schemas.aereoPuerto import PostAereoPuerto, AereoPuertos

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/aereoPuerto",
    tags=["aereoPuerto"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create(request: Request, item: PostAereoPuerto):
    return {"msg": "Registro exitoso"}

@router.put("/{id}")
async def update(request: Request, id: int, item: PostAereoPuerto):
    return {"msg": "Actualizacion exitosa"}

@router.delete("/{id}")
async def delete(request: Request, id: int):
    return {"msg": "Borrado exitosamente"}

@router.get("/all", response_model=AereoPuertos)
async def get_all(request: Request):
    return ""

@router.get("/estado/{id}", response_model=AereoPuertos)
async def get_por_estado(request: Request, id: int):
    return {"msg": "Borrado exitosamente"}