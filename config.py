import os

class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_API_URL='https://newsapi.org/v2/everything?q=Africa&apiKey={}'
    NEWS_API_KEY = '6951ecff678145af8f875a69f2abbdd7'
    SECRET_KEY = 'voke'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}