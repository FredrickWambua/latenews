class Top_headlines:
    '''
    NewsSource class to define the News source Objects
    '''
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url= url


class Article:
    '''
    Articles class model to define the article Objects
    '''
    def __init__(self, title, source, urlToImage, desrciption, author, publishedAt, url, content):
        self.title = title
        self.source = source
        self.urlToImage =urlToImage
        self.description = desrciption
        self.author = author
        self.publishedAt = publishedAt
        self.url = url
        self.content =content


