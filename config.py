import os

class Config:
    '''
    This is the general configuration parent class
    '''
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'

    EVERYTHING_END_POINT = 'everything/'
    TOP_HEADLINES_END_POINT = 'top-headlines/'
    CATEGORY_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

    API_KEY = os.environ.get('API_KEY')


class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}