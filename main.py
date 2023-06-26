from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sql.database import engine, Base
from routes.obras import router_obras
from routes.login import login_router
from routes.register import router_register
from routes.concept import concept_router
from routes.catalogs import catalog_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=[
                   '*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'], )
app.title = "Cityworks API"
app.version = "0.0.1"
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


app.include_router(router_obras)
app.include_router(login_router)
app.include_router(router_register)
app.include_router(concept_router)
app.include_router(catalog_router)


@app.get("/", response_class=HTMLResponse)
def read_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
