from decouple import config


class Config():
    SECRET_KEY = config('SECRET_KEY')
    CLOUD_NAME = config('CLOUD_NAME')
    API_KEY = config('API_KEY')
    API_SECRET = config('API_SECRET')



class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
