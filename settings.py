import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = '123456'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv('IP', 'localhost:5050')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True