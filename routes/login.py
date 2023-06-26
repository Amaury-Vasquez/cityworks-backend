from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from sql.database import get_db
from models.main import Usuario
from sqlalchemy.orm import Session
from schemas.user import UserLogin, User
from schemas.custom import ErrorMessage

login_router = APIRouter(
    prefix="/api/v1/login", tags=["login"], responses={404: {"description": "Not found"}}
)


@login_router.post("/", response_class=JSONResponse, status_code=200, responses={200: {"model": User}, 401: {"model": ErrorMessage}, 500: {"model": ErrorMessage}})
def get_user(user_data: UserLogin, response: Response, db: Session = Depends(get_db)):
    try:
        result: UserLogin = db.query(Usuario).filter(
            Usuario.email == user_data.email).first()
        if (result.password == user_data.password):
            return result
        response.status_code = 401
        return {
            "message": "Usuario o contraseña incorrectos"
        }
    except Exception as e:
        response.status_code = 500
        return {
            "message": "Error en el servidor"
        }
