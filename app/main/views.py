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

@main.route('/profile')
def profle():

    '''
    View root page function that returns the index page and its data
    '''
    top_article=get_articles()
    
    return render_template('profile.html',articles= top_article)
@main.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news()
    print(news_sources)
    title = 'Home'
    return render_template('login.html', title = title, sources = news_sources )
@main.route('/register')
def article():

    '''
    View root page function that returns the index page and its data
    '''
    top_article=get_articles()
    print(top_article)
    return render_template('register.html',articles= top_article)