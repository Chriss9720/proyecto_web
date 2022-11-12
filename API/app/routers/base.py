from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()

@router.get("/")
async def status(request: Request):
    return {"API": "ARRIBA"}