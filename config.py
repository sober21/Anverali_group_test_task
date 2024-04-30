import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jsdfh73410)(*kjfkjanlk'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    FLASK_ADMIN_SWATCH = os.environ.get('FLASK_ADMIN_SWATCH') or 'cerulean'
