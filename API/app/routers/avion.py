from fastapi import APIRouter, Depends, Request

from services.avion import AvionService

from schemas.user import User
from schemas.Avion import PostAvion, GetAvion, Avion, Escalas

from utils.auth import get_current_user
from utils.service_result import handle_result

from configs.database import get_db

router = APIRouter(
    prefix="/avion",
    tags=["avion"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create(request: Request, item: PostAvion, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    result = handle_result(AvionService(db).crear(item))
    return result

@router.put("/{id}")
async def update(request: Request, id: int, item: Escalas, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    return {"msg": "Registro exitoso"}

@router.get("/all", response_model=GetAvion)
async def get_all(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    return ""

@router.get("/by_id/{id}", response_model=Avion)
async def get_all(request: Request, id: int, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    return ""

@router.get("/ruta/{origen}/{destino}", response_model=GetAvion)
async def get_ruta(request: Request, db: get_db = Depends(), current_user: User = Depends(get_current_user)):
    return ""