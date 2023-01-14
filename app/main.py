from fastapi import FastAPI
from core.db.session import engine
from core.db.base_class import Base
from core.api.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_routers(app):
    app.include_router(api_router)


def start_app():
    app = FastAPI(description="""
    API para conocer el stock, provedor, precios de nuestras frutas
    """, title="API de Frutas 2023 v1")
    create_tables()
    include_routers(app)
    return app


app = start_app()
