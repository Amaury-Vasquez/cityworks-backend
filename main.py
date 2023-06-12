from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql.models import Base
from sql.database import engine, SessionLocal
from routes.obras import router_obras

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "Cityworks API"
app.version = "0.0.1"
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


app.include_router(router_obras)


@app.get("/", response_class=HTMLResponse)
def read_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})