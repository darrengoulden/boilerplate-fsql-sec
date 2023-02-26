# Third party imports
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Flask config variables
    """
    APP = os.environ.get('FLASK_APP')
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = os.environ.get('TEMPLATES_FOLDER')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    
    """
    Database
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """
    Flask Security Too
    """
    # Core
    SECURITY_FLASH_MESSAGES = True # Specifies whether or not to flash messages during security procedures.
    SECURITY_SHOW_MENU = True
    # Login/Logout
    SECURITY_LOGIN_URL = "/login"
    SECURITY_LOGOUT_URL = "/logout"
    SECURITY_POST_LOGIN_VIEW = '/'
    SECURITY_POST_LOGOUT_VIEW = '/'
    SECURITY_UNAUTHORIZED_VIEW = None
    # Registerable
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome'
    SECURITY_POST_REGISTER_VIEW = None
    SECURITY_USERNAME_ENABLE = False
    SECURITY_USERNAME_REQUIRED = False
    # Confirmable
    SECURITY_CONFIRMABLE = True
    SECURITY_CONFIRM_EMAIL_WITHIN = '5 days'
    SECURITY_EMAIL_SUBJECT_CONFIRM = 'Please confirm your email'
    SECURITY_POST_CONFIRM_VIEW = None
    # Changeable
    SECURITY_CHANGEABLE = True
    SECURITY_POST_CHANGE_VIEW = None
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = True
    SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = 'Your password has been changed'
    # Recoverable
    SECURITY_RECOVERABLE = True
    SECURITY_POST_RESET_VIEW = None
    SECURITY_RESET_VIEW = None
    SECURITY_RESET_PASSWORD_WITHIN = '5 days'
    SECURITY_SEND_PASSWORD_RESET_EMAIL = True
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = True
    SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = 'Password reset instructions'
    SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = 'Your password has been reset'
    # Trackable
    SECURITY_TRACKABLE = True
    # Social Oauth
    SECURITY_OAUTH_ENABLE = False
    SECURITY_OAUTH_BUILTIN_PROVIDERS = ["google"]
    
    """
    Flask-Mailman
    """
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEBUG = True
    MAIL_BACKEND = 'file'
    MAIL_SUPPRESS_SEND = False
    MAIL_FILE_PATH = '/Users/daz/github/boilerplate-fsql-sec'

class ProdConfig(Config):
    DEBUG = os.environ.get('FLASK_DEBUG')
    TESTING = False


class DevConfig(Config):
    DEBUG = os.environ.get('FLASK_DEBUG')
    TESTING = True