from pydantic import BaseModel, constr

from utils.regex import Regex

class Credential(BaseModel):
    username: str
    password: str

class UserData(BaseModel):
    first_name : str
    last_name : str
    email : str
    rfc : constr(min_length=13, max_length=14)
    curp : str

class User(UserData):
    id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserRegister(UserCreate):
    nombre: constr(strict=True, regex=Regex.name, min_length=1, max_length=255)
    apellido_paterno: constr(strict=True, regex=Regex.name, min_length=1, max_length=255)
    apellido_materno: constr(strict=True, regex=Regex.name, min_length=1, max_length=255)
    correo: str
    empleado: bool

    def to_dict():
        return {
            "nombre": "str",
            "apellido_paterno": "str",
            "apellido_materno": "str",
            "correo": "str",
            "empleado": True,
            "username": "str",
            "password": "str"
        }