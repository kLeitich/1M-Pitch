import os

class Config:
    SECRET_KEY = 'voke'
    SQLALCHEMY_TRACK_MODIFICATION = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1421@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "kevokaksz@gmail.com"
    MAIL_PASSWORD = "moringaproject2"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}