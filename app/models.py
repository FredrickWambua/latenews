class Source:
    '''
    Source class to define the News source Objects
    '''
    def __init__(self, id, name, description, source_url):
        self.id = id
        self.name = name
        self.description= description
        self.url = source_url


class Article:
    '''
    Articles class model to define the article Objects
    '''
    def __init__(self, title, urlToImage, desrciption, author, publishedAt, url, content):
        self.title = title
        self.urlToImage =urlToImage
        self.description = desrciption
        self.author = author
        self.publishedAt = publishedAt
        self.url = url
        self.content =content

class Category:
    '''
    Article class inistance for categories objects of the news sources
    '''
    def __init__(self, title, urlToImage, desrciption, author, publishedAt, url, content):
        self.title = title
        self.urlToImage =urlToImage
        self.description = desrciption
        self.author = author
        self.publishedAt = publishedAt
        self.url = url
        self.content =content
