from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import Article,NewsSource

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html' )

@main.route('/register')
def register():

    '''
    View root page function that returns the index page and its data
    '''
   
    
    return render_template('register.html')
@main.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('login.html')
@main.route('/profile')
def profile():

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('profile.html')