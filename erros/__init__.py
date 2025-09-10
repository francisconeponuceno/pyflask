from flask import Flask
from .views import error_bp

def init_app(app: Flask):
    app.register_blueprint(error_bp)