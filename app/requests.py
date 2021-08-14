
import json, urllib.request
from requests import get
from .models import Source, Article

base_url = None
api_key = None
def config_request(app):
    global base_url, api_key

    base_url = app.config['NEWS_SOURCE_URL']
    EVERYTHING_END_POINT = 'everything/'
    TOP_HEADLINES_END_POINT = 'top-headlines/'
    api_key = app.config['API_KEY']


def get_news_objects():

    url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=ffc5892b0e01428f8dd49bca764e3fd9'

    req_url = url.format(api_key)
    
    with urllib.request.urlopen(req_url) as url:

        get_data = url.read()
        news_data_response = json.loads(get_data)

        sources_results = None
        if news_data_response['sources']:
            results_list = news_data_response['sources']
            sources_results = process_sources(results_list)


    return sources_results

def process_sources(results_list):
    source_results = []
    for source_item in results_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description= source_item.get('description')
        source_url= source_item.get('url')



        sources = Source(id,name,description,source_url)
        source_results.append(sources)

    return source_results


def get_articles(source):
    url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=ffc5892b0e01428f8dd49bca764e3fd9'

    req_url = url.format(source, api_key)
   
    
    with urllib.request.urlopen(req_url) as url:

        get_data = url.read()
        news_data_response = json.loads(get_data)
        sources_results = None
        if news_data_response['articles']:
    
            results_list = news_data_response['articles']
            sources_results = process_articles(results_list)


    return sources_results    

def process_articles(article_list):
    news_object = []
    for item in article_list:
        title = item.get('title')
        urlToImage = item.get('urlToImage')
        description = item.get('description')
        author = item.get('author')
        publishedAt = item.get('publishedAt')
        url = item.get('url')
        content = item.get('content')

        obj = Article(title, urlToImage, description, author, publishedAt, url, content)
        news_object.append(obj)
    
    return news_object


