import os

class Config:
    SECRET_KEY = 'voke'
    SQLALCHEMY_TRACK_MODIFICATION = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1421@localhost/pitch'



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}