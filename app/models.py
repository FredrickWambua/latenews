class NewsSource:
    '''
    NewsSource class to define the News source Objects
    '''
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url= url


class Articles:
    '''
    Articles class to define the article Objects
    '''
    def __init__(self, title, image, desrciption, author, time, url):
        self.title = title
        self.image =image
        self.description = desrciption
        self.author = author
        self.time = time
        self.url = url


