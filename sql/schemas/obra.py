from pydantic import BaseModel


class BaseObra(BaseModel):
    nombre_obra: str
    id_obra: str


class LeeObra(BaseObra):
    class Config:
        orm_mode = True
