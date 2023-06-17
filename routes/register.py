from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from sql.database import get_db
from sql.models import Usuario
from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas.user import UserRegister


def create_user_id(user: UserRegister):
    pre_hashed = user.email + user.rol + user.nombre
    hashed = str(hash(pre_hashed))[1:11]
    print(hashed)
    return hashed


router_register = APIRouter(prefix="/api/v1/register",
                            tags=["register"], responses={404: {"description": "Not created"}})


@router_register.post("/", response_class=JSONResponse, status_code=201)
def register_user(user: UserRegister, response: Response, db: Session = Depends(get_db)):
    try:
        db_user = Usuario(email=user.email, password=user.password,
                          nombre=user.nombre, apellido=user.apellido, rol=user.rol, id_usuario=create_user_id(user))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        exists = e.find('duplicate')
        response.status_code = 400
        if exists != -1:
            return {
                "message": "Este correo ya esta registrado"
            }
        return {
            "message": "Informacion mal procesada"
        }
