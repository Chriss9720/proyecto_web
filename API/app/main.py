from routers import user
from utils.app_exceptions import AppExceptionCase
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import base, token, piloto, pais_estado, aereoPuerto, avion, asientos, boletos
from configs.database import create_tables

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from fastapi.security import OAuth2PasswordBearer

from utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
)
from utils.app_exceptions import app_exception_handler

# Es el ORM que te genera todas las tablas declaradas en el modelo
create_tables()

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="API para la materia de web",
    description="FastAPI template implementa las 4 operaciones basicas de CRUD",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)

app.include_router(base.router)
app.include_router(token.router)
app.include_router(user.router)
app.include_router(piloto.router)
app.include_router(pais_estado.router)
app.include_router(aereoPuerto.router)
app.include_router(avion.router)
app.include_router(asientos.router)
app.include_router(boletos.router)