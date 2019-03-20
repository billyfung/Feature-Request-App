import os


class BaseConfig:

    PROJECT = 'feature_request'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = '/tmp/feature_request/logs'

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = '/tmp/uploads'


class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin@localhost/features'
    

class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
