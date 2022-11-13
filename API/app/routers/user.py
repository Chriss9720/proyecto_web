from fastapi import APIRouter, Request, Depends

from services.user import UserService

from schemas.user import UserRegister

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
async def registro(request: Request, item: UserRegister, db: get_db = Depends()):
    result = handle_result(UserService(db).create_user(item))
    return result

@router.get("/")
async def get(request: Request, id:int):
    return UserRegister.to_dict()

@router.put("/")
async def update(request: Request, item: UserRegister):
    return {"msg": "Actualizacion exitosa"}

@router.delete("/")
async def delete(request: Request):
    return {"msg": "Baja exitosa"}