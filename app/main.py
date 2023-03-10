from fastapi import FastAPI
from core.db.session import engine
from core.db.base_class import Base
from core.api.base import api_router
from web.base import web_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



def create_tables():
    Base.metadata.create_all(bind=engine)

def configure_static(app):
    app.mount('/static', StaticFiles(directory="static"), name="static")

def include_routers(app):
    app.include_router(api_router, responses={
        404:{"description": "No Encontrado"},
        422:{"description": "La Data enviada no es valida"},
        500:{"description": "Entidad improcesable"},
    })
    app.include_router(web_router)

def start_app():
    app = FastAPI(description="""
    API de Bodega
    """, title="API de Bodega 2023 v1")

    origins = [
    "http://127.0.0.1:8000",
    "https://test-dos.diego-luque.com/",
    "http://test-dos.diego-luque.com/"
    ]

    create_tables()

    include_routers(app)
    configure_static(app)

    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    return app


app = start_app()



