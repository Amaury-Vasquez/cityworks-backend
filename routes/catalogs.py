from fastapi import APIRouter, Depends, Response
from typing import List
from sql.database import get_db
from schemas.catalogo import CatalogoModel, CreaCatalogoModel, ConceptosEnCatalogoModel
from models.main import Catalogo, ConceptoEnCatalogo, Conceptos
from schemas.concepto import Concepto
from modules.hash_strings import hash_id

catalog_router = APIRouter(prefix="/api/v1/catalogs",
                           tags=["catalog"], responses={404: {"description": "Not found", 500: {"message": "Error en el servidor"}}})


@catalog_router.get("/", status_code=200, responses={200: {"model": List[CatalogoModel]}})
def get_all_catalogs(response: Response, db=Depends(get_db)):
    try:
        result = db.query(Catalogo).all()
        return result
    except Exception as e:
        response.status_code = 500


@catalog_router.get("/{id}", status_code=200, responses={200: {"model": CatalogoModel}})
def get_catalog_by_id(id: str, response: Response, db=Depends(get_db)):
    try:
        result = db.query(Catalogo).filter(Catalogo.id == id).first()
        if result:
            return result
        response.status_code = 404
    except Exception as e:
        response.status_code = 500


@catalog_router.post("/", status_code=201, responses={201: {"model": CatalogoModel}})
def create_catalog(catalog: CreaCatalogoModel, response: Response, db=Depends(get_db)):
    try:
        nombre, fecha, id_superintendente = catalog.nombre, catalog.fecha, catalog.id_superintendente
        id = nombre + id_superintendente
        new_catalog = Catalogo(id=hash_id(
            id, 20), id_superintendente=id_superintendente, nombre=nombre, fecha=fecha)
        db.add(new_catalog)
        db.commit()
        db.refresh(new_catalog)
        return new_catalog
    except Exception as e:
        response.status_code = 500


@catalog_router.get("/{id}/items", status_code=200, responses={200: {"model": List[Concepto]}})
def get_all_concepts_from_catalog(id: str, response: Response, db=Depends(get_db)):
    try:
        catalog = db.query(Catalogo).filter(Catalogo.id == id).first()
        db_catalog = db.query(ConceptoEnCatalogo).filter(
            ConceptoEnCatalogo.catalogo == id).all()
        if db_catalog and db_catalog != []:
            concepts = []
            for concept in db_catalog:
                db_concept = db.query(Conceptos).filter(
                    Conceptos.clave == concept.clave).first()
                concepts.append(db_concept)
            return {
                "catalogo": catalog,
                "conceptos": concepts
            }
        response.status_code = 404
    except Exception as e:
        print(e)


@catalog_router.post('/{id}', status_code=201, responses={201: {"model": Concepto}})
def add_concept_to_catalog(id: str, concept: str, response: Response, db=Depends(get_db)):
    try:
        db_catalog = db.query(Catalogo).filter(Catalogo.id == id).first()
        db_concept = db.query(Conceptos).filter(
            Conceptos.clave == concept).first()
        if (db_catalog and db_concept):
            new_concept = ConceptoEnCatalogo(
                catalogo=id, clave=concept)
            db.add(new_concept)
            db.commit()
            db.refresh(new_concept)
            return new_concept
        response.status_code = 404
    except Exception as e:
        print(e)
        response.status_code = 500


@catalog_router.delete("/{id}", status_code=200, responses={202: {"model": CatalogoModel}})
def delete_catalog(id: str, response: Response, db=Depends(get_db)):
    try:
        db_catalog = db.query(Catalogo).filter(Catalogo.id == id).first()
        if db_catalog:
            db.delete(db_catalog)
            db.commit()
            return db_catalog
        response.status_code = 404

    except Exception as e:
        response.status_code = 500
