from fastapi import APIRouter, Depends, Response
from typing import List
from fastapi.responses import JSONResponse
from sql.database import get_db
from sql.models import Conceptos
from schemas.concepto import Concepto, CreaConcepto, ModificaConcepto
from schemas.custom import ErrorMessage
from modules.hash_strings import hash_id

concept_router = APIRouter(
    prefix="/api/v1/concepts", tags=["concept"], responses={404: {"description": "Not found"}}
)


@concept_router.get("/",  status_code=200, response_class=JSONResponse, responses={200: {"model": List[Concepto]}, 500: {"model": ErrorMessage}})
def get_all_concepts(response: Response, db=Depends(get_db)):
    try:
        result = db.query(Conceptos).all()
        return result
    except Exception as e:
        response.status_code = 500
        return {
            "message": "Error en el servidor"
        }


@concept_router.get("/{id}", status_code=200, response_class=JSONResponse, responses={200: {"model": Concepto}, 404: {"model": ErrorMessage}, 500: {"model": ErrorMessage}})
def get_concept(id: str, response: Response, db=Depends(get_db)):
    try:
        db_concept = db.query(Conceptos).filter(Conceptos.clave == id).first()
        if (db_concept):
            return db_concept
        response.status_code = 404
        return {
            "message": "No se encontro el concepto"
        }
    except Exception as e:
        return {
            "message": "Error en el servidor"
        }


@concept_router.post("/", status_code=201, response_class=JSONResponse, responses={201: {"model": Concepto}, 500: {"model": ErrorMessage}})
def create_concept(concept: CreaConcepto, response: Response, db=Depends(get_db)):
    try:
        nombre, unidad, precio, cantidad, descripcion = concept.nombre, concept.unidad, concept.precio, concept.cantidad, concept.descripcion
        clave = hash_id(nombre + unidad + str(precio) + str(cantidad))
        importe = precio * cantidad
        db_concept = Conceptos(nombre=nombre, unidad=unidad, precio=precio, cantidad=cantidad, descripcion=descripcion,
                               clave=clave, importe=importe)
        db.add(db_concept)
        db.commit()
        db.refresh(db_concept)
        return db_concept
    except Exception as e:
        response.status_code = 500
        return {
            "message": "Error en el servidor"
        }


@concept_router.delete("/{id}", status_code=200, response_class=JSONResponse, responses={200: {"model": Concepto}, 404: {"model": ErrorMessage}, 500: {"model": ErrorMessage}})
def delete_concept(id: str, response: Response, db=Depends(get_db)):
    try:
        db_concept = db.query(Conceptos).filter(Conceptos.clave == id).first()
        if (db_concept):
            db.delete(db_concept)
            db.commit()
            return db_concept
        response.status_code = 404
        return {
            "message": "No se encontro el concepto"
        }
    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "message": "Error en el servidor"
        }


@concept_router.patch("/{id}", status_code=200, response_class=JSONResponse, responses={200: {"model": Concepto}, 404: {"model": ErrorMessage}, 500: {"model": ErrorMessage}})
def update_concept(id: str, updated_concept: ModificaConcepto,  response: Response, db=Depends(get_db)):
    try:
        db_concept = db.query(Conceptos).filter(Conceptos.clave == id).first()
        if (db_concept):
            for key, value in updated_concept.dict().items():
                if (value != None):
                    setattr(db_concept, key, value)
            db.commit()
            db.refresh(db_concept)
            return db_concept
        response.status_code = 404
        return {
            "message": "No se encontro el concepto"
        }
    except Exception as e:
        response.status_code = 500
        return {
            "message": "Error en el servidor"
        }
