import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

Base = declarative_base()

# Obtener la URI de la base de datos desde la variable de entorno
DATABASE_URI = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db_session = SessionLocal()

def init_db(app):
    Base.metadata.create_all(bind=engine)
    app.teardown_appcontext(close_db)

def close_db(exception=None):
    # db_session.remove()
    pass
