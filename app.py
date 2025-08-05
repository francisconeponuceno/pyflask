from flask import Flask, abort
from config import Config
from errors.views import error_bp
import errors


def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)

    errors.init_app(app)
    
    @app.route('/')
    def index():
        return 'olá mundo'


    @app.route('/erro')
    def error_page():
        abort(code=500)
        return 'Bem dindo'
    
    
    return app