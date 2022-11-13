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
async def get(request: Request, id:int, db: get_db = Depends()):
    result = handle_result(UserService(db).get_by_id(id))
    return result

@router.put("/{id}")
async def update(request: Request, id: int, item: UserRegister, db: get_db = Depends()):
    result = handle_result(UserService(db).update(id, item))
    return result

@router.delete("/{id}")
async def delete(request: Request, id: int, db: get_db = Depends()):
    result = handle_result(UserService(db).deleted(id))
    return result