from fastapi import APIRouter, Depends, Request

from schemas.Avion import PostAvion, GetAvion, Avion

from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/avion",
    tags=["avion"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create(request: Request, item: PostAvion):
    return {"msg": "Registro exitoso"}

@router.post("/{id}")
async def update(request: Request, id:int, item: PostAvion):
    return {"msg": "Registro exitoso"}

@router.get("/all", response_model=GetAvion)
async def get_all(request: Request):
    return ""

@router.get("/by_id/{id}", response_model=Avion)
async def get_all(request: Request, id: int):
    return ""

@router.get("/ruta/{origen}/{destino}", response_model=GetAvion)
async def get_ruta(request: Request):
    return ""