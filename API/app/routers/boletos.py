from fastapi import APIRouter, Depends, Request

from schemas.user import User
from schemas.boletos import Boletos

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/boletos",
    tags=["boletos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=Boletos)
async def create(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    return {"msg": "Registro exitoso"}