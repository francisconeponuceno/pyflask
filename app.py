from flask import Flask, abort
from config import Config
from erros.views import error_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)

    app.register_blueprint(blueprint=error_bp)
    
    
    @app.route('/')
    def index():
        return 'olá mundo'


    @app.route('erro')
    def erro_page():
        abort(code=404)
        return 'Bem dindo'
    
    
    return app