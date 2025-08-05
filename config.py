import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    if FLASK_ENV == "development":
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    elif FLASK_ENV == "production":
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

