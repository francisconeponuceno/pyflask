from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)
    

    # Extenção
    return app