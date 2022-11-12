from fastapi import APIRouter, Depends, Request

from schemas.boletos import Boletos

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/boletos",
    tags=["boletos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=Boletos)
async def create(request: Request):
    return {"msg": "Registro exitoso"}