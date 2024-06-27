from flask import Flask
from .config import Config
from .database import db
from .auth import auth_blueprint
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    jwt = JWTManager(app)  # Inicializar JWTManager
    CORS(app)  # Habilitar CORS para toda la aplicación
    
    migrate = Migrate(app, db)  # Inicializar Flask-Migrate
    
    app.register_blueprint(auth_blueprint)
    
    return app
