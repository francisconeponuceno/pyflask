# pip install flask-debugtoolbar
from flask import Flask, abort
from config import Config
import errors
from extensions import toolbar

def create_app():
    app = Flask(__name__)
    app.config.from_object(obj=Config)

    if app.debug:
        toolbar.init_app(app)

    errors.init_app(app)
    
    @app.route('/')
    def index():
        return '''
            <body>
                <h1>Olá Mundo!</h1> 
            </body>
        '''


    @app.route('/erro')
    def error_page():
        abort(code=500)
        return 'Bem dindo'
    
    
    return app