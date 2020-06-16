import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = ''.join([basedir, '/.env'])
load_dotenv(dotenv_path)


class Config(object):
    # Flask
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Deploy on Heroku
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
