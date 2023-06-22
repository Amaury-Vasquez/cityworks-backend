from pydantic import BaseModel
from typing import Optional


class Concepto(BaseModel):
    clave: str = "0123456789"
    nombre: str = "Concepto"
    unidad: str = "m2"
    precio: float = 100
    cantidad: int = 200
    importe: float = precio * cantidad
    descripcion: Optional[str] = None


class CreaConcepto(BaseModel):
    nombre: str = "Concepto"
    unidad: str = "m2"
    precio: float = 100
    cantidad: int = 200
    descripcion: Optional[str]


class ModificaConcepto(BaseModel):
    nombre: Optional[str] = "Modificado"
    unidad: Optional[str] = "m3"
    precio: Optional[float] = 200
    cantidad: Optional[int] = 300
    descripcion: Optional[str] = "Agrega descripcion"
