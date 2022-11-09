from fastapi import APIRouter, Depends, Request
from schemas.user import User
from utils.auth import get_current_user

from services.foo import FooService
from schemas.foo import FooItem, FooItemCreate
from typing import List
from utils.service_result import handle_result

from slowapi import Limiter
from slowapi.util import get_remote_address

from configs.database import get_db

limiter = Limiter(key_func=get_remote_address)

router = APIRouter(
    prefix="/foos",
    tags=["Foos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=FooItem, summary="Devuelve un objeto de tipo Foo con el id indicado en el parametro, devuelve un error si no existe")
@limiter.limit("2/minute")
async def get_item(request: Request, id: int, db: get_db = Depends(), user: User = Depends(get_current_user)):
    result = FooService(db).get_item(id)
    return handle_result(result)


@router.get("/", response_model=List[FooItem], summary="Devuelve todos los objetos de tipo Foo, devuelve un arreglo vacio si no existen")
@limiter.limit("2/minute")
async def get_all(request: Request, db: get_db = Depends(), user: User = Depends(get_current_user)):
    result = FooService(db).get_all()
    return handle_result(result)

@router.post("/", response_model=FooItem, status_code=201, summary="Crea un objeto de tipo Foo con los datos enviados en el body, devuelve un error si ya existe")
@limiter.limit("2/minute")
async def create_item(request: Request, item: FooItemCreate, db: get_db = Depends(), user: User = Depends(get_current_user)):
    result = FooService(db).create_item(item)
    return handle_result(result)

@router.put("/{id}", response_model=FooItem, status_code=200,summary="Actualiza un objeto de tipo Foo con los datos enviados en el body, devuelve un error si no existe")
@limiter.limit("2/minute")
async def update_item(request: Request, id: int, item: FooItemCreate, db: get_db = Depends(), user: User = Depends(get_current_user)):
    result = FooService(db).update_item(id, item)
    return handle_result(result)

@router.delete("/{id}", response_model=FooItem, summary="Elimina un objeto de tipo Foo con el id indicado en el parametro, devuelve un error si no existe")
@limiter.limit("2/minute")
async def delete_item(request: Request, id: int, item: FooItemCreate, db: get_db = Depends(), user: User = Depends(get_current_user)):
    result = FooService(db).delete_item(id)
    return handle_result(result)