from pydantic import BaseModel
from typing import Optional


class CatalogoModel(BaseModel):
    id: str = "0123456789"
    id_superintendente: str = "usuario123"
    nombre: str = "Catalogo ejemplo"
    fecha: str = "2023-06-25"


class CreaCatalogoModel(BaseModel):
    id_superintendente: str = "1154075801"
    nombre: str = "Cimientos"
    fecha: str = "2023-06-25"


class ConceptosEnCatalogoModel(BaseModel):
    id_catalogo: str = "1154075801"
    clave_concepto: str = "0054679964"
    id: int = 1
