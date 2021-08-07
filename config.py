import os

class Config:
    '''
    This is the general configuration parent class
    '''
    API_SOURCE_URL = ''
    CATEGORY_URL = ''
    API_KEY = ''


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