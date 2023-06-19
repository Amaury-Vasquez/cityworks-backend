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


class User(BaseModel):
    nombre: str = "John"
    email: str = "ejemplo@mail.com"
    apellido: str = "Doe"
    rol: str = "superintendente"
    id_usuario: str = "1020304050"
