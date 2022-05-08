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

def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_url.format(api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_article_results(article_results_list)


    return article_results

def process_article_results(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    article_results = []
    for article_item in article_list:
        topic = article_item.get('title')
        name = article_item.get('name')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        content = article_item.get('content')

        if url:
            article_object = Article(topic,name,description,url,urlToImage,date,content)
            print(article_object)
            article_results.append(article_object)

    return article_results

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('catergory')
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = NewsSource(name,description,url,category,language,country)
            news_results.append(news_object)

    return news_results