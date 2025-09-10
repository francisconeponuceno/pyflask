import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
<<<<<<< HEAD
    DEBUG_TO_ENABLED = True
    DEBUG_TO_INTERCEPT_REDIRECTS = False
=======
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
>>>>>>> 9d5ee9a48893bea55668029a91f3e3f729f3f050


    #if FLASK_ENV == "development":
    #    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    #elif FLASK_ENV == "production":
    #    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

