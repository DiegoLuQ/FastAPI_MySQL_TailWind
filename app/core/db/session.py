from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

sqlalchemy_database_url = settings.RUTA_MYSQL

url_db = "mysql+pymysql://root@localhost:33306/test_frutas"
engine = create_engine(sqlalchemy_database_url)

#estudiar
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
