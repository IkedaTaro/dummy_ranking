import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = False
