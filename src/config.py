import os
from dotenv import load_dotenv

# Cargas variables de entorno
load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://mi_usuario:mi_contraseña@localhost/mi_base_datos'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
