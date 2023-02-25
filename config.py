# Third party imports
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Set Flask config variables."""
    APP = os.environ.get('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = os.environ.get('TEMPLATES_FOLDER')

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    TESTING = True