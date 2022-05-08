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
