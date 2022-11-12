from fastapi import APIRouter, Request

from schemas.user import UserRegister

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def registro(request: Request, item: UserRegister):
    return {"msg": "Registro exitoso"}

@router.get("/")
async def get(request: Request, id:int):
    return UserRegister.to_dict()

@router.put("/")
async def update(request: Request, item: UserRegister):
    return {"msg": "Actualizacion exitosa"}

@router.delete("/")
async def delete(request: Request):
    return {"msg": "Baja exitosa"}