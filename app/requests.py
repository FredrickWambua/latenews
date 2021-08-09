import urllib.request, json
from .models import NewsSource, Articles

# getting api key
api_key = None

# getting news base url
base_url = None

# top headlines url
top_headlines_url = None

def configure_requests(app):
    global api_key, base_url
    api_key = app.config['API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']
    top_headlines_url = app.config['TOP_HEADLINES_URL']


def get_news_source():
    '''
    function to getting the source data in json format to the url request
    '''
    get_news_source = base_url.format(api_key)

    with urllib.request.urlopen(get_news_source) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['news_sources']:
            news_source_results_list = get_news_source_response['news_sources']
            news_source_results = process_results(news_source_results_list)

    return news_source_results

def process_results(news_source_list):
    '''
    The function to process results and convert them to a list of objects
    Args:
        news_source_list: dictionary with news source details
    Returns:
        news_source_results: A list of news source objects
    '''
    news_source_results =[]
    for news_source_item in news_source_list:
        id = news_source_item.get('id')
        name = news_source_item.get('name')

        if id:
            news_source_object = NewsSource(id, name)
            news_source_results.append(news_source_object)
    
    return news_source_results
