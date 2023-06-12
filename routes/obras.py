from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sql.database import get_db
from sql.models import Obra
from sqlalchemy.orm import Session

router_obras = APIRouter(
    prefix="/api/v1/obras", tags=["obras"], responses={404: {"description": "Not found"}})


@router_obras.get("/", response_class=JSONResponse, status_code=200)
def get_obras(db: Session = Depends(get_db)):
    print(db)
    return db.query(Obra).all()
