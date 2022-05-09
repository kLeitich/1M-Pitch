from . import db

class NewsSource:
     
    '''
    NewsSource class to define news Objects
    '''

    def __init__(self,name,description,url,category,langauge,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.langauge = langauge
        self.country = country

class Article:
    def __init__(self,title,name, author,description, url, image, date):
        self.title = title
        self.name = name
        self.author = author 
        self.description = description
        self.url = url
        self.image = image 
        self.date = date
        # self.intro = intro

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'