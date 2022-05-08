import urllib.request,json
from .models import NewsSource,Article
from app import models

api_key = None
base_url = None
article_url= None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    print(api_key)
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_URL']

