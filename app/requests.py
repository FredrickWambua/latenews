import json
from requests import get
from .models import Top_headlines, Article

def get_news_objects(api_key, endpoint, base_url, query_str):
    req_url = base_url.format(endpoint,api_key,query_str)
    response = get(req_url)
    news_data = json.loads(response.text)
    articles = news_data('articles')

    return articles

def the_news_objects(article_list):
    news_object = []
    for item in article_list:
        title = item.get('title')
        source = item.get('source')
        urlToImage = item.get('urlToImage')
        description = item.get('description')
        author = item.get('author')
        publishedAt = item.get('publishedAt')
        url = item.get('url')
        content = item.get('content')

        obj = Article(title, source, urlToImage, description, author, publishedAt, url, content)
        the_news_objects.append(obj)
    
    return the_news_objects


