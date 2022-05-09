import os



class Config:
    SECRET_KEY = 'TheDifference'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sniffer:sniff@localhost/thepitches'

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sniffer:sniff@localhost/watchlist_test'

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sniffer:sniff@localhost/thepitches'
    DEBUG = True
    
config_options ={
    'development': DevConfig,
    'production': ProdConfig,
    # 'test': TestConfig
}        