from flask import render_template,request,redirect,url_for
from . import main
from ..models import User,Role

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('index.html')

@main.route('/profile')
def profle():

    '''
    View root page function that returns the index page and its data
    '''
   
    
    return render_template('profile.html')
@main.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    
    return render_template('login.html')
@main.route('/register')
def article():

    '''
    View root page function that returns the index page and its data
    '''
   
    return render_template('register.html')