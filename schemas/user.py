from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str


class UserRegister(BaseModel):
    nombre: str
    email: str
    apellido: str
    password: str
    rol: str
