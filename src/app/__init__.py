from flask import Flask
from flask_cors import CORS
from .db import init_db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('config.Config')

    init_db(app) # Iniciar la BD con la app

    register_routes(app) # Registrar las rutas 

    return app