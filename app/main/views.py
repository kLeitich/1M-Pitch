from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import Article,NewsSource

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news()
   
    title = 'Home'
    return render_template('index.html', title = title, sources = news_sources )

@main.route('/trending')
def trending():

    '''
    View root page function that returns the index page and its data
    '''
    top_article=get_articles()
    
    return render_template('trending.html',articles= top_article)
@main.route('/source')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news()
    print(news_sources)
    title = 'Home'
    return render_template('source.html', title = title, sources = news_sources )
@main.route('/article')
def article():

    '''
    View root page function that returns the index page and its data
    '''
    top_article=get_articles()
    print(top_article)
    return render_template('article.html',articles= top_article)